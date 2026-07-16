from __future__ import annotations

import json
import time
from collections import Counter
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime, timedelta
from pathlib import Path

from game_news.dedupe import cluster_articles
from game_news.discovery import collect_candidates
from game_news.http import HttpClient
from game_news.models import AppConfig, Article, SourceConfig, SourceResult
from game_news.normalize import (
    domain_of,
    normalize_url,
    normalize_whitespace,
    stable_id,
    title_from_url,
)
from game_news.parsers import parse_datetime
from game_news.scoring import classify_and_score
from game_news.site import build_site
from game_news.storage import (
    append_unique_articles,
    load_articles,
    now_iso,
    read_json,
    write_json_atomic,
)

# Confirmed manually by the repository owner on 2026-07-16.
DROPPED_SOURCE_IDS = {
    "playliner-com",
    "appmetrica-yandex-ru",
    "appmetrica-yandex-com",
    "press-kwalee-com",
    "rbc-ru",
}


def _within_days(value: str | None, days: int) -> bool:
    parsed = parse_datetime(value)
    return parsed is not None and parsed >= datetime.now(UTC) - timedelta(days=days)


def _failure_kind(error: str | None, attempts: list[dict], rejection_summary: dict[str, int]) -> str:
    text = " ".join([error or "", *(str(item.get("error") or "") for item in attempts)]).lower()
    if "403" in text or "forbidden" in text or "cloudflare" in text:
        return "blocked"
    if "401" in text or "unauthorized" in text:
        return "unauthorized"
    if "429" in text or "too many requests" in text:
        return "rate_limited"
    if "timeout" in text or "timed out" in text:
        return "timeout"
    if "name resolution" in text or "dns" in text or "resolve host" in text:
        return "dns"
    if "ssl" in text or "certificate" in text or "tls" in text:
        return "tls"
    if rejection_summary.get("too_old", 0) > 0:
        return "no_recent_articles"
    if rejection_summary.get("missing_date", 0) > 0:
        return "missing_dates"
    if rejection_summary.get("invalid_url", 0) > 0:
        return "invalid_articles"
    if any(
        str(item.get("stage", "")).startswith(("feed", "sitemap"))
        and item.get("outcome") == "ok"
        and int(item.get("item_count") or 0) > 0
        for item in attempts
    ):
        return "no_recent_articles"
    if any(item.get("outcome") == "empty" for item in attempts):
        return "no_articles_found"
    return "unknown"


def _candidate_reason(candidate: dict, source: SourceConfig, config: AppConfig) -> tuple[str | None, str | None]:
    raw_url = str(candidate.get("url") or "").strip()
    if not raw_url:
        return "missing_url", None
    canonical = normalize_url(raw_url, source.home_url)
    if not canonical.startswith(("http://", "https://")):
        return "invalid_url", canonical
    published_at = candidate.get("published_at")
    if not published_at:
        return "missing_date", canonical
    if parse_datetime(published_at) is None:
        return "unparseable_date", canonical
    if not _within_days(published_at, config.max_age_days):
        return "too_old", canonical
    return None, canonical


def _article_from_candidate(
    source: SourceConfig,
    candidate: dict,
    config: AppConfig,
    discovered_at: str,
    canonical: str,
) -> Article:
    published_at = candidate.get("published_at")
    title = normalize_whitespace(str(candidate.get("title") or title_from_url(canonical)))
    summary = normalize_whitespace(str(candidate.get("summary") or ""))[:1200]
    date_confidence = str(candidate.get("date_confidence") or "none")
    topics, score = classify_and_score(
        title=title,
        summary=summary,
        source_priority=source.priority,
        source_tags=source.tags,
        topics=config.topics,
        date_confidence=date_confidence,
    )
    return Article(
        id=stable_id(canonical),
        url=canonical,
        canonical_url=canonical,
        title=title,
        source_id=source.id,
        source_name=source.name,
        source_domain=domain_of(canonical) or source.domain,
        source_category=source.category,
        source_priority=source.priority,
        published_at=published_at,
        discovered_at=discovered_at,
        date_source=str(candidate.get("date_source") or "unknown"),
        date_confidence=date_confidence,
        summary=summary,
        author=normalize_whitespace(str(candidate.get("author") or "")),
        language=source.language,
        matched_topics=topics,
        importance_score=score,
        origin="collector",
    )


def _manual_check_for(
    source: SourceConfig,
    method: str,
    feeds: list[str],
    sitemaps: list[str],
    attempts: list[dict],
    failure_kind: str | None,
    rejection_summary: dict[str, int],
) -> dict | None:
    if failure_kind == "no_recent_articles":
        return None

    successful_feed = next(
        (
            attempt.get("final_url") or attempt.get("url")
            for attempt in attempts
            if str(attempt.get("stage", "")).startswith("feed")
            and attempt.get("outcome") == "ok"
        ),
        None,
    )
    successful_sitemap = next(
        (
            attempt.get("final_url") or attempt.get("url")
            for attempt in attempts
            if str(attempt.get("stage", "")).startswith("sitemap")
            and attempt.get("outcome") == "ok"
        ),
        None,
    )
    homepage_attempt = next((item for item in attempts if item.get("stage") == "homepage"), None)
    final_home = (homepage_attempt or {}).get("final_url")
    redirected_domain = domain_of(str(final_home or ""))
    expected_domain = source.domain.removeprefix("www.")

    if redirected_domain and redirected_domain.removeprefix("www.") != expected_domain:
        return {
            "priority": "high",
            "reason": "redirected_to_other_domain",
            "url": source.home_url,
            "instruction": f"Открыть источник и подтвердить, что редирект на {redirected_domain} ожидаем. Если бренд поглощён или закрыт — удалить либо объединить источник.",
        }
    if successful_feed and rejection_summary.get("missing_date", 0):
        return {
            "priority": "high",
            "reason": "feed_items_without_dates",
            "url": str(successful_feed),
            "instruction": "Открыть RSS и проверить названия полей даты у первых 3 элементов. Сохранить XML или сообщить фактический тег даты.",
        }
    if successful_feed and rejection_summary.get("unparseable_date", 0):
        return {
            "priority": "high",
            "reason": "unparseable_feed_dates",
            "url": str(successful_feed),
            "instruction": "Открыть RSS и прислать пример значения даты, которое не распознаётся.",
        }
    if failure_kind == "blocked":
        return {
            "priority": "medium",
            "reason": "blocked_on_github_runner",
            "url": feeds[0] if feeds else source.home_url,
            "instruction": "Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.",
        }
    if successful_sitemap:
        return {
            "priority": "medium",
            "reason": "sitemap_needs_path_filter",
            "url": str(successful_sitemap),
            "instruction": "Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.",
        }
    if method != "none" and successful_feed:
        return {
            "priority": "medium",
            "reason": "feed_reachable_but_no_accepted_items",
            "url": str(successful_feed),
            "instruction": "Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.",
        }
    return {
        "priority": "low",
        "reason": "source_structure_unknown",
        "url": source.home_url,
        "instruction": "Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.",
    }


def _collect_source(
    source: SourceConfig,
    config: AppConfig,
    known_urls: set[str],
) -> tuple[list[Article], SourceResult]:
    started = time.perf_counter()
    checked_at = now_iso()
    attempts: list[dict] = []
    try:
        client = HttpClient(config.user_agent, config.timeout_seconds)
        candidates, method, feeds, sitemaps, attempts = collect_candidates(
            source, client, config.max_age_days
        )
        articles: list[Article] = []
        accepted_urls: set[str] = set()
        rejection_summary: Counter[str] = Counter()
        rejection_examples: dict[str, list[str]] = {}

        for candidate in candidates:
            reason, canonical = _candidate_reason(candidate, source, config)
            if reason:
                rejection_summary[reason] += 1
                example = canonical or str(candidate.get("url") or candidate.get("title") or "")
                if example:
                    rejection_examples.setdefault(reason, [])
                    if len(rejection_examples[reason]) < 3:
                        rejection_examples[reason].append(example)
                continue
            assert canonical is not None
            if canonical in accepted_urls:
                rejection_summary["duplicate_in_source"] += 1
                continue
            accepted_urls.add(canonical)
            articles.append(_article_from_candidate(source, candidate, config, checked_at, canonical))

        new_count = sum(1 for article in articles if article.canonical_url not in known_urls)
        status = "ok" if articles else "warning"
        error = None if articles else "No accepted recent dated articles"
        summary_dict = dict(sorted(rejection_summary.items()))
        failure_kind = None if articles else _failure_kind(error, attempts, summary_dict)
        manual_check = None
        if not articles:
            manual_check = _manual_check_for(
                source, method, feeds, sitemaps, attempts, failure_kind, summary_dict
            )
        return articles, SourceResult(
            source_id=source.id,
            source_name=source.name,
            status=status,
            checked_at=checked_at,
            method=method,
            fetched_count=len(candidates),
            accepted_count=len(articles),
            new_count=new_count,
            elapsed_ms=round((time.perf_counter() - started) * 1000),
            discovered_feeds=feeds,
            discovered_sitemaps=sitemaps,
            error=error,
            failure_kind=failure_kind,
            attempts=attempts,
            rejection_summary=summary_dict,
            rejection_examples=rejection_examples,
            manual_check=manual_check,
        )
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        failure_kind = _failure_kind(error, attempts, {})
        return [], SourceResult(
            source_id=source.id,
            source_name=source.name,
            status="error",
            checked_at=checked_at,
            elapsed_ms=round((time.perf_counter() - started) * 1000),
            error=error,
            failure_kind=failure_kind,
            attempts=attempts,
            manual_check=_manual_check_for(source, "none", [], [], attempts, failure_kind, {}),
        )


def _select_sources(
    config: AppConfig,
    source_ids: Iterable[str] | None,
    all_sources: bool,
) -> list[SourceConfig]:
    active_sources = [source for source in config.sources if source.id not in DROPPED_SOURCE_IDS]
    requested = set(source_ids or [])
    if requested:
        dropped = requested & DROPPED_SOURCE_IDS
        if dropped:
            raise ValueError(f"Dropped source ids cannot be collected: {', '.join(sorted(dropped))}")
        unknown = requested - {source.id for source in active_sources}
        if unknown:
            raise ValueError(f"Unknown source ids: {', '.join(sorted(unknown))}")
        return [source for source in active_sources if source.id in requested]
    if all_sources:
        return active_sources
    return [source for source in active_sources if source.enabled]


def _write_diagnostics(public_dir: Path, generated_at: str, results: list[SourceResult]) -> None:
    failures = Counter(result.failure_kind or "none" for result in results if result.status != "ok")
    payload = {
        "schema_version": 2,
        "generated_at": generated_at,
        "source_count": len(results),
        "dropped_sources": sorted(DROPPED_SOURCE_IDS),
        "failure_summary": dict(sorted(failures.items())),
        "sources": [result.to_dict() for result in results],
    }
    write_json_atomic(public_dir / "diagnostics.json", payload)

    lines = [
        "# Диагностика источников",
        "",
        f"Обновлено: `{generated_at}`",
        "",
        f"Исключено вручную: **{len(DROPPED_SOURCE_IDS)}**",
        "",
        "## Сводка",
        "",
    ]
    for kind, count in sorted(failures.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{kind}`: **{count}**")
    lines.extend(["", "## Проблемные источники", ""])
    for result in results:
        if result.status == "ok":
            continue
        lines.extend(
            [
                f"### {result.source_name} (`{result.source_id}`)",
                "",
                f"- Статус: `{result.status}`",
                f"- Категория: `{result.failure_kind or 'unknown'}`",
                f"- Метод: `{result.method}`",
                f"- Получено кандидатов: `{result.fetched_count}`",
                f"- Принято: `{result.accepted_count}`",
                f"- Причины отбраковки: `{json.dumps(result.rejection_summary, ensure_ascii=False)}`",
                f"- Время: `{result.elapsed_ms} ms`",
                f"- Ошибка: `{result.error or 'нет'}`",
                f"- Попыток: `{len(result.attempts)}`",
                "",
            ]
        )
        for attempt in result.attempts:
            lines.append(
                f"  - `{attempt.get('stage')}` → `{attempt.get('outcome')}` — "
                f"{attempt.get('url')}"
                + (f" — {attempt.get('error')}" if attempt.get("error") else "")
            )
        lines.append("")
    (public_dir / "diagnostics.md").write_text("\n".join(lines), encoding="utf-8")

    checks = [result for result in results if result.manual_check]
    manual_payload = {
        "schema_version": 1,
        "generated_at": generated_at,
        "count": len(checks),
        "checks": [
            {
                "source_id": result.source_id,
                "source_name": result.source_name,
                "failure_kind": result.failure_kind,
                **(result.manual_check or {}),
            }
            for result in checks
        ],
    }
    write_json_atomic(public_dir / "manual-checks.json", manual_payload)

    manual_lines = [
        "# Что желательно проверить вручную",
        "",
        f"Обновлено: `{generated_at}`",
        "",
        "Источники с обычным статусом `no_recent_articles` сюда не включаются: они технически исправны, но не публиковались в текущем окне.",
        "",
    ]
    priority_order = {"high": 0, "medium": 1, "low": 2}
    for result in sorted(
        checks,
        key=lambda item: (
            priority_order.get(str((item.manual_check or {}).get("priority")), 9),
            item.source_name.casefold(),
        ),
    ):
        check = result.manual_check or {}
        manual_lines.extend(
            [
                f"## {result.source_name} (`{result.source_id}`)",
                "",
                f"- Приоритет: **{check.get('priority', 'low')}**",
                f"- Причина: `{check.get('reason', 'unknown')}`",
                f"- Проверить: {check.get('url', result.source_id)}",
                f"- Действие: {check.get('instruction', 'Проверить структуру источника.')}",
                f"- Отбраковка: `{json.dumps(result.rejection_summary, ensure_ascii=False)}`",
                "",
            ]
        )
    (public_dir / "manual-checks.md").write_text("\n".join(manual_lines), encoding="utf-8")


def collect(
    config: AppConfig,
    root: Path,
    window_hours: int | None = None,
    source_ids: Iterable[str] | None = None,
    dry_run: bool = False,
    strict_min_success: int = 0,
    all_sources: bool = False,
) -> dict:
    articles_path = root / "data/articles.jsonl"
    state_path = root / "data/state.json"
    public_dir = root / "public"
    selected_sources = _select_sources(config, source_ids, all_sources)
    existing = load_articles(articles_path)
    known_urls = {article.canonical_url for article in existing}

    all_candidates: list[Article] = []
    results: list[SourceResult] = []
    with ThreadPoolExecutor(max_workers=min(config.max_workers, max(1, len(selected_sources)))) as executor:
        futures = {
            executor.submit(_collect_source, source, config, known_urls): source
            for source in selected_sources
        }
        for future in as_completed(futures):
            articles, result = future.result()
            all_candidates.extend(articles)
            results.append(result)

    results.sort(key=lambda result: result.source_name.casefold())
    success_count = sum(1 for result in results if result.status == "ok")
    if strict_min_success and success_count < strict_min_success:
        raise RuntimeError(
            f"Only {success_count} sources succeeded; strict minimum is {strict_min_success}"
        )

    generated_at = now_iso()
    if dry_run:
        return {
            "generated_at": generated_at,
            "sources": [result.to_dict() for result in results],
            "candidate_count": len(all_candidates),
            "new_count": sum(1 for article in all_candidates if article.canonical_url not in known_urls),
        }

    combined, added_count = append_unique_articles(articles_path, all_candidates)
    hours = window_hours or config.latest_window_hours
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    recent = [
        article
        for article in combined
        if article.origin == "collector"
        and (parse_datetime(article.published_at) or datetime.min.replace(tzinfo=UTC)) >= cutoff
    ]
    clustered = cluster_articles(recent, config.title_similarity_threshold)

    latest_payload = {
        "schema_version": 1,
        "generated_at": generated_at,
        "window_hours": hours,
        "article_count": len(clustered),
        "raw_article_count": len(recent),
        "new_urls_this_run": added_count,
        "articles": [article.to_dict() for article in clustered],
    }
    write_json_atomic(public_dir / "latest.json", latest_payload)
    archive_date = datetime.now(UTC).date().isoformat()
    write_json_atomic(public_dir / "archive" / f"{archive_date}.json", latest_payload)

    status_payload = {
        "schema_version": 3,
        "generated_at": generated_at,
        "source_count": len(results),
        "dropped_sources": sorted(DROPPED_SOURCE_IDS),
        "ok": sum(1 for result in results if result.status == "ok"),
        "warning": sum(1 for result in results if result.status == "warning"),
        "error": sum(1 for result in results if result.status == "error"),
        "failure_summary": dict(
            Counter(result.failure_kind or "none" for result in results if result.status != "ok")
        ),
        "manual_check_count": sum(1 for result in results if result.manual_check),
        "sources": [result.to_dict() for result in results],
    }
    write_json_atomic(public_dir / "status.json", status_payload)
    _write_diagnostics(public_dir, generated_at, results)

    state = read_json(state_path, {"schema_version": 1, "last_run_at": None, "sources": {}})
    state["last_run_at"] = generated_at
    source_state = state.setdefault("sources", {})
    for dropped_id in DROPPED_SOURCE_IDS:
        source_state.pop(dropped_id, None)
    for result in results:
        previous = source_state.get(result.source_id, {})
        consecutive_errors = int(previous.get("consecutive_errors", 0))
        if result.status == "error":
            consecutive_errors += 1
        else:
            consecutive_errors = 0
        source_state[result.source_id] = {
            "last_checked_at": result.checked_at,
            "status": result.status,
            "method": result.method,
            "new_count": result.new_count,
            "consecutive_errors": consecutive_errors,
            "last_error": result.error,
            "failure_kind": result.failure_kind,
            "discovered_feeds": result.discovered_feeds,
            "discovered_sitemaps": result.discovered_sitemaps,
            "rejection_summary": result.rejection_summary,
            "manual_check": result.manual_check,
        }
    write_json_atomic(state_path, state)
    build_site(public_dir)

    run_log = {
        "generated_at": generated_at,
        "selected_sources": len(selected_sources),
        "dropped_sources": sorted(DROPPED_SOURCE_IDS),
        "successful_sources": success_count,
        "candidate_count": len(all_candidates),
        "added_count": added_count,
        "latest_count": len(clustered),
        "manual_check_count": status_payload["manual_check_count"],
        "failure_summary": status_payload["failure_summary"],
    }
    (public_dir / "collection-run.log").write_text(
        json.dumps(run_log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return {**run_log, "status": status_payload}
