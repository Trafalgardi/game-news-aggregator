from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any
from urllib.parse import urljoin

from game_news.http import HttpClient
from game_news.models import SourceConfig
from game_news.parsers import (
    discover_feed_links,
    discover_sitemap_links,
    parse_article_metadata,
    parse_datetime,
    parse_feed,
    parse_html_listing,
    parse_sitemap,
)

COMMON_FEED_PATHS = ("feed", "rss", "rss.xml", "feed.xml", "atom.xml")


def _is_recent(date_value: str | None, max_age_days: int) -> bool:
    parsed = parse_datetime(date_value)
    if parsed is None:
        return False
    return parsed >= datetime.now(UTC) - timedelta(days=max_age_days)


def _attempt(
    attempts: list[dict[str, Any]],
    *,
    stage: str,
    url: str,
    outcome: str,
    status_code: int | None = None,
    final_url: str | None = None,
    content_type: str | None = None,
    item_count: int | None = None,
    error: str | None = None,
) -> None:
    attempts.append(
        {
            "stage": stage,
            "url": url,
            "outcome": outcome,
            "status_code": status_code,
            "final_url": final_url,
            "content_type": content_type,
            "item_count": item_count,
            "error": error,
        }
    )


def _try_feed(
    feed_url: str,
    stage: str,
    source: SourceConfig,
    client: HttpClient,
    attempts: list[dict[str, Any]],
) -> tuple[list[dict], str | None]:
    try:
        response = client.get(feed_url, source.request_delay_seconds)
        items = parse_feed(response.text)
        _attempt(
            attempts,
            stage=stage,
            url=feed_url,
            outcome="ok" if items else "empty",
            status_code=response.status_code,
            final_url=response.url,
            content_type=response.content_type,
            item_count=len(items),
        )
        return items, response.url
    except Exception as exc:
        _attempt(
            attempts,
            stage=stage,
            url=feed_url,
            outcome="error",
            error=f"{type(exc).__name__}: {exc}",
        )
        return [], None


def collect_candidates(
    source: SourceConfig,
    client: HttpClient,
    max_age_days: int,
) -> tuple[list[dict], str, list[str], list[str], list[dict[str, Any]]]:
    attempts: list[dict[str, Any]] = []
    discovered_feeds = list(dict.fromkeys(source.feed_urls))
    discovered_sitemaps = list(dict.fromkeys(source.sitemap_urls))

    # Explicit feeds are attempted before the homepage. This lets a source work
    # even when its front page blocks GitHub-hosted runners with 403/Cloudflare.
    for feed_url in list(discovered_feeds):
        items, final_url = _try_feed(feed_url, "feed-configured", source, client, attempts)
        if final_url and final_url not in discovered_feeds:
            discovered_feeds.append(final_url)
        if items:
            return (
                items[: source.max_items],
                "feed-configured",
                discovered_feeds,
                discovered_sitemaps,
                attempts,
            )

    home_html = ""
    homepage_url = source.home_url
    try:
        homepage = client.get(source.home_url, source.request_delay_seconds)
        home_html = homepage.text
        homepage_url = homepage.url
        _attempt(
            attempts,
            stage="homepage",
            url=source.home_url,
            outcome="ok",
            status_code=homepage.status_code,
            final_url=homepage.url,
            content_type=homepage.content_type,
        )
        discovered_feeds.extend(discover_feed_links(home_html, homepage.url))
        discovered_feeds = list(dict.fromkeys(discovered_feeds))
    except Exception as exc:
        _attempt(
            attempts,
            stage="homepage",
            url=source.home_url,
            outcome="error",
            error=f"{type(exc).__name__}: {exc}",
        )

    attempted_feed_urls = {
        str(item["url"])
        for item in attempts
        if str(item.get("stage", "")).startswith("feed-")
    }
    for feed_url in discovered_feeds:
        if feed_url in attempted_feed_urls:
            continue
        items, final_url = _try_feed(feed_url, "feed-discovered", source, client, attempts)
        if final_url and final_url not in discovered_feeds:
            discovered_feeds.append(final_url)
        if items:
            return items[: source.max_items], "feed", discovered_feeds, discovered_sitemaps, attempts

    for path in COMMON_FEED_PATHS:
        feed_url = urljoin(homepage_url.rstrip("/") + "/", path)
        if feed_url in attempted_feed_urls or feed_url in discovered_feeds:
            continue
        items, final_url = _try_feed(feed_url, "feed-common", source, client, attempts)
        if final_url and final_url not in discovered_feeds:
            discovered_feeds.append(final_url)
        if items:
            return (
                items[: source.max_items],
                "feed-common",
                discovered_feeds,
                discovered_sitemaps,
                attempts,
            )

    if home_html:
        listing_items = parse_html_listing(home_html, homepage_url)
        recent_listing = [
            item for item in listing_items if _is_recent(item.get("published_at"), max_age_days)
        ]
        _attempt(
            attempts,
            stage="html-listing",
            url=homepage_url,
            outcome="ok" if recent_listing else "empty",
            item_count=len(recent_listing),
        )
        if recent_listing:
            return (
                recent_listing[: source.max_items],
                "html-listing",
                discovered_feeds,
                discovered_sitemaps,
                attempts,
            )

    robots_url = urljoin(homepage_url, "/robots.txt")
    try:
        robots = client.get(robots_url, source.request_delay_seconds)
        found = discover_sitemap_links(robots.text, homepage_url)
        discovered_sitemaps.extend(found)
        _attempt(
            attempts,
            stage="robots",
            url=robots_url,
            outcome="ok",
            status_code=robots.status_code,
            final_url=robots.url,
            content_type=robots.content_type,
            item_count=len(found),
        )
    except Exception as exc:
        _attempt(
            attempts,
            stage="robots",
            url=robots_url,
            outcome="error",
            error=f"{type(exc).__name__}: {exc}",
        )

    if not discovered_sitemaps:
        discovered_sitemaps.append(urljoin(homepage_url, "/sitemap.xml"))
    discovered_sitemaps = list(dict.fromkeys(discovered_sitemaps))

    sitemap_urls: list[dict] = []
    for sitemap_url in discovered_sitemaps[:6]:
        try:
            response = client.get(sitemap_url, source.request_delay_seconds)
            kind, entries = parse_sitemap(response.text)
            _attempt(
                attempts,
                stage="sitemap",
                url=sitemap_url,
                outcome="ok" if entries else "empty",
                status_code=response.status_code,
                final_url=response.url,
                content_type=response.content_type,
                item_count=len(entries),
            )
            if kind == "index":
                recent_indexes = sorted(
                    entries,
                    key=lambda entry: entry.get("lastmod") or "",
                    reverse=True,
                )[:6]
                for index_entry in recent_indexes:
                    child_url = index_entry["url"]
                    try:
                        child = client.get(child_url, source.request_delay_seconds)
                        child_kind, child_entries = parse_sitemap(child.text)
                        _attempt(
                            attempts,
                            stage="sitemap-child",
                            url=child_url,
                            outcome="ok" if child_entries else "empty",
                            status_code=child.status_code,
                            final_url=child.url,
                            content_type=child.content_type,
                            item_count=len(child_entries),
                        )
                        if child_kind == "urls":
                            sitemap_urls.extend(child_entries)
                    except Exception as exc:
                        _attempt(
                            attempts,
                            stage="sitemap-child",
                            url=child_url,
                            outcome="error",
                            error=f"{type(exc).__name__}: {exc}",
                        )
            elif kind == "urls":
                sitemap_urls.extend(entries)
        except Exception as exc:
            _attempt(
                attempts,
                stage="sitemap",
                url=sitemap_url,
                outcome="error",
                error=f"{type(exc).__name__}: {exc}",
            )

    recent_urls = [entry for entry in sitemap_urls if _is_recent(entry.get("lastmod"), max_age_days)]
    recent_urls.sort(key=lambda entry: entry.get("lastmod") or "", reverse=True)
    enriched: list[dict] = []
    for entry in recent_urls[: min(source.max_items, 12)]:
        article_url = entry["url"]
        try:
            response = client.get(article_url, source.request_delay_seconds)
            metadata = parse_article_metadata(response.text, response.url)
            if not metadata.get("published_at"):
                metadata["published_at"] = entry.get("lastmod")
                metadata["date_source"] = "sitemap_lastmod"
                metadata["date_confidence"] = "low"
            enriched.append(metadata)
            _attempt(
                attempts,
                stage="article-enrich",
                url=article_url,
                outcome="ok",
                status_code=response.status_code,
                final_url=response.url,
                content_type=response.content_type,
                item_count=1,
            )
        except Exception as exc:
            _attempt(
                attempts,
                stage="article-enrich",
                url=article_url,
                outcome="error",
                error=f"{type(exc).__name__}: {exc}",
            )
    if enriched:
        return enriched, "sitemap", discovered_feeds, discovered_sitemaps, attempts

    return [], "none", discovered_feeds, discovered_sitemaps, attempts
