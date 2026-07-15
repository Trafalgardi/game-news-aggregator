from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from game_news.models import AppConfig, SourceConfig

DEFAULT_SOURCES_PATH = Path("config/sources.yaml")
DEFAULT_KEYWORDS_PATH = Path("config/keywords.yaml")


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with path.open("r", encoding="utf-8") as stream:
        value = yaml.safe_load(stream) or {}
    if not isinstance(value, dict):
        raise ValueError(f"Configuration root must be an object: {path}")
    return value


def load_config(
    sources_path: Path = DEFAULT_SOURCES_PATH,
    keywords_path: Path = DEFAULT_KEYWORDS_PATH,
) -> AppConfig:
    raw_sources = _load_yaml(sources_path)
    raw_keywords = _load_yaml(keywords_path)
    settings = raw_sources.get("settings", {})

    sources: list[SourceConfig] = []
    seen_ids: set[str] = set()
    seen_domains: set[str] = set()
    for raw in raw_sources.get("sources", []):
        source = SourceConfig(
            id=str(raw["id"]),
            name=str(raw["name"]),
            domain=str(raw["domain"]).lower(),
            home_url=str(raw.get("home_url") or f"https://{raw['domain']}/"),
            category=str(raw.get("category", "industry")),
            enabled=bool(raw.get("enabled", True)),
            priority=int(raw.get("priority", 50)),
            language=str(raw.get("language", "en")),
            tags=list(raw.get("tags", [])),
            feed_urls=list(raw.get("feed_urls", [])),
            sitemap_urls=list(raw.get("sitemap_urls", [])),
            max_items=int(raw.get("max_items", settings.get("max_items_per_source", 50))),
            request_delay_seconds=float(raw.get("request_delay_seconds", 0.0)),
        )
        if source.id in seen_ids:
            raise ValueError(f"Duplicate source id: {source.id}")
        if source.domain in seen_domains:
            raise ValueError(f"Duplicate source domain: {source.domain}")
        if not source.home_url.startswith(("http://", "https://")):
            raise ValueError(f"home_url must be HTTP(S): {source.id}")
        if not 0 <= source.priority <= 100:
            raise ValueError(f"priority must be between 0 and 100: {source.id}")
        seen_ids.add(source.id)
        seen_domains.add(source.domain)
        sources.append(source)

    return AppConfig(
        user_agent=str(
            settings.get(
                "user_agent",
                "GameNewsAggregator/1.0 (+https://github.com/OWNER/game-news-aggregator)",
            )
        ),
        timeout_seconds=int(settings.get("timeout_seconds", 20)),
        max_workers=int(settings.get("max_workers", 6)),
        max_age_days=int(settings.get("max_age_days", 7)),
        latest_window_hours=int(settings.get("latest_window_hours", 36)),
        title_similarity_threshold=int(settings.get("title_similarity_threshold", 92)),
        sources=sources,
        topics=dict(raw_keywords.get("topics", {})),
    )


def validate_config(config: AppConfig) -> list[str]:
    errors: list[str] = []
    enabled = [source for source in config.sources if source.enabled]
    if not enabled:
        errors.append("At least one source must be enabled")
    if config.max_workers < 1:
        errors.append("max_workers must be positive")
    if config.latest_window_hours < 1:
        errors.append("latest_window_hours must be positive")
    if not config.topics:
        errors.append("At least one topic must be configured")
    return errors
