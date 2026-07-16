from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class SourceConfig:
    id: str
    name: str
    domain: str
    home_url: str
    category: str
    enabled: bool = True
    priority: int = 50
    language: str = "en"
    tags: list[str] = field(default_factory=list)
    feed_urls: list[str] = field(default_factory=list)
    sitemap_urls: list[str] = field(default_factory=list)
    max_items: int = 50
    request_delay_seconds: float = 0.0


@dataclass(slots=True)
class AppConfig:
    user_agent: str
    timeout_seconds: int
    max_workers: int
    max_age_days: int
    latest_window_hours: int
    title_similarity_threshold: int
    sources: list[SourceConfig]
    topics: dict[str, dict[str, Any]]


@dataclass(slots=True)
class Article:
    id: str
    url: str
    canonical_url: str
    title: str
    source_id: str
    source_name: str
    source_domain: str
    source_category: str
    source_priority: int
    published_at: str | None
    discovered_at: str
    date_source: str
    date_confidence: str
    summary: str = ""
    author: str = ""
    language: str = ""
    matched_topics: list[str] = field(default_factory=list)
    importance_score: int = 0
    duplicate_of: str | None = None
    duplicate_urls: list[str] = field(default_factory=list)
    duplicate_sources: list[str] = field(default_factory=list)
    origin: str = "collector"
    telegram_post: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class SourceResult:
    source_id: str
    source_name: str
    status: str
    checked_at: str
    method: str = "none"
    fetched_count: int = 0
    accepted_count: int = 0
    new_count: int = 0
    elapsed_ms: int = 0
    error: str | None = None
    failure_kind: str | None = None
    discovered_feeds: list[str] = field(default_factory=list)
    discovered_sitemaps: list[str] = field(default_factory=list)
    attempts: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def utc_iso(value: datetime) -> str:
    value = value.astimezone().replace(microsecond=0)
    return value.isoformat().replace("+00:00", "Z")
