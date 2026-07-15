from __future__ import annotations

import json
import os
import tempfile
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from game_news.models import Article


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def load_articles(path: Path) -> list[Article]:
    if not path.exists():
        return []
    articles: list[Article] = []
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
                articles.append(Article(**raw))
            except (json.JSONDecodeError, TypeError) as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return articles


def write_articles(path: Path, articles: Iterable[Article]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            for article in articles:
                stream.write(json.dumps(article.to_dict(), ensure_ascii=False, separators=(",", ":")))
                stream.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def append_unique_articles(path: Path, new_articles: list[Article]) -> tuple[list[Article], int]:
    existing = load_articles(path)
    known = {article.canonical_url for article in existing}
    added = 0
    for article in new_articles:
        if article.canonical_url in known:
            continue
        existing.append(article)
        known.add(article.canonical_url)
        added += 1
    existing.sort(key=lambda article: (article.published_at or article.discovered_at, article.id))
    write_articles(path, existing)
    return existing, added


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
