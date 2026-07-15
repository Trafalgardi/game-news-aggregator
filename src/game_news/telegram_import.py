from __future__ import annotations

import json
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from game_news.models import Article
from game_news.normalize import (
    domain_of,
    normalize_url,
    normalize_whitespace,
    stable_id,
    title_from_url,
)
from game_news.parsers import iso_utc, parse_datetime
from game_news.storage import append_unique_articles, now_iso

URL_RE = re.compile(r"https?://[^\s<>\"\]\)]+", re.IGNORECASE)


def _iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _iter_strings(item)
    elif isinstance(value, dict):
        for child in value.values():
            yield from _iter_strings(child)


def import_telegram_export(input_path: Path, articles_path: Path) -> tuple[int, int]:
    with input_path.open("r", encoding="utf-8") as stream:
        export = json.load(stream)

    channel_name = normalize_whitespace(str(export.get("name") or "Telegram export"))
    imported: list[Article] = []
    seen: set[str] = set()
    for message in export.get("messages", []):
        urls: list[str] = []
        for key in ("text", "text_entities", "caption", "caption_entities"):
            for value in _iter_strings(message.get(key, [])):
                urls.extend(URL_RE.findall(value))
        date = iso_utc(parse_datetime(message.get("date")))
        for raw_url in urls:
            try:
                canonical = normalize_url(raw_url)
            except ValueError:
                continue
            if not canonical.startswith(("http://", "https://")) or canonical in seen:
                continue
            seen.add(canonical)
            message_id = message.get("id")
            imported.append(
                Article(
                    id=stable_id(canonical),
                    url=canonical,
                    canonical_url=canonical,
                    title=title_from_url(canonical),
                    source_id=f"legacy-{domain_of(canonical).replace('.', '-')}",
                    source_name=channel_name,
                    source_domain=domain_of(canonical),
                    source_category="historical_import",
                    source_priority=0,
                    published_at=date,
                    discovered_at=date or now_iso(),
                    date_source="telegram_message_date",
                    date_confidence="medium",
                    summary="",
                    language="",
                    matched_topics=[],
                    importance_score=0,
                    origin="telegram_import",
                    telegram_post=(
                        f"https://t.me/hyper_casual_news/{message_id}" if message_id is not None else None
                    ),
                )
            )

    _, added = append_unique_articles(articles_path, imported)
    return len(imported), added
