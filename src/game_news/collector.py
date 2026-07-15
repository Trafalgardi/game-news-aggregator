from __future__ import annotations

import time
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


def _within_days(value: str | None, days: int) -> bool:
    parsed = parse_datetime(value)
    return parsed is not None and parsed >= datetime.now(UTC) - timedelta(days=days)


def _article_from_candidate(
    source: SourceConfig,
    candidate: dict,
    config: AppConfig,
    discovered_at: str,
) -> Article | None:
    raw_url = str(candidate.get("url") or "").strip()
    if not raw_url:
        return None
    canonical = normalize_url(raw_url, source.home_url)
    if not canonical.startswith(("http://", "https://")):
        return None
    published_at = candidate.get("published_at")
    if not _within_days(published_at, config.max_age_days):
        return None
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


def _collect_source(source: SourceConfig, config: AppConfig, known_urls: set[str]) -> tuple[list[Article], SourceResult]:
    started = time.perf_counter()
    checked_at = now_iso()
    try:
        client = HttpClient(config.user_agent, config.timeout_seconds)
        candidates, method, feeds, sitemaps = collect_candidates(source, client, config.max_age_days)
        articles: list[Article] = []
        accepted_urls: set[str] = set()
        for candidate in candidates:
            article = _article_from_candidate(source, candidate, config, checked_at)
            if article is None or article.canonical_url in accepted_urls:
                continue
            accepted_urls.add(article.canonical_url)
            articles.append(article)
        new_count = sum(1 for article in articles if article.canonical_url not in known_urls)
        status = "ok" if articles else "warning"
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
            error=None if articles else "No recent dated articles found",
        )
    except Exception as exc:
        return [], SourceResult(
            source_id=source.id,
            source_name=source.name,
            status="error",
            checked_at=checked_at,
            elapsed_ms=round((time.perf_counter() - started) * 1000),
            error=f"{type(exc).__name__}: {exc}",
        )


def _select_sources(config: AppConfig, source_ids: Iterable[str] | None) -> list[SourceConfig]:
    requested = set(source_ids or [])
    if requested:
        unknown = requested - {source.id for source in config.sources}
        if unknown:
            raise ValueError(f"Unknown source ids: {', '.join(sorted(unknown))}")
        return [source for source in config.sources if source.id in requested]
    return [source for source in config.sources if source.enabled]


def collect(
    config: AppConfig,
    root: Path,
    window_hours: int | None = None,
    source_ids: Iterable[str] | None = None,
    dry_run: bool = False,
    strict_min_success: int = 0,
) -> dict:
    articles_path = root / "data/articles.jsonl"
    state_path = root / "data/state.json"
    public_dir = root / "public"
    selected_sources = _select_sources(config, source_ids)
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
        "schema_version": 1,
        "generated_at": generated_at,
        "source_count": len(results),
        "ok": sum(1 for result in results if result.status == "ok"),
        "warning": sum(1 for result in results if result.status == "warning"),
        "error": sum(1 for result in results if result.status == "error"),
        "sources": [result.to_dict() for result in results],
    }
    write_json_atomic(public_dir / "status.json", status_payload)

    state = read_json(state_path, {"schema_version": 1, "last_run_at": None, "sources": {}})
    state["last_run_at"] = generated_at
    source_state = state.setdefault("sources", {})
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
            "discovered_feeds": result.discovered_feeds,
            "discovered_sitemaps": result.discovered_sitemaps,
        }
    write_json_atomic(state_path, state)
    build_site(public_dir)

    return {
        "generated_at": generated_at,
        "selected_sources": len(selected_sources),
        "successful_sources": success_count,
        "candidate_count": len(all_candidates),
        "added_count": added_count,
        "latest_count": len(clustered),
        "status": status_payload,
    }
