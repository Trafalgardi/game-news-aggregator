from __future__ import annotations

from datetime import UTC, datetime, timedelta
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


def collect_candidates(
    source: SourceConfig,
    client: HttpClient,
    max_age_days: int,
) -> tuple[list[dict], str, list[str], list[str]]:
    homepage = client.get(source.home_url, source.request_delay_seconds)
    home_html = homepage.text

    discovered_feeds = list(source.feed_urls)
    discovered_feeds.extend(discover_feed_links(home_html, homepage.url))
    discovered_feeds = list(dict.fromkeys(discovered_feeds))

    for feed_url in discovered_feeds:
        try:
            response = client.get(feed_url, source.request_delay_seconds)
            items = parse_feed(response.text)
            if items:
                return items[: source.max_items], "feed", discovered_feeds, list(source.sitemap_urls)
        except Exception:
            continue

    if not discovered_feeds:
        for path in COMMON_FEED_PATHS:
            feed_url = urljoin(homepage.url.rstrip("/") + "/", path)
            try:
                response = client.get(feed_url, source.request_delay_seconds)
                items = parse_feed(response.text)
                if items:
                    discovered_feeds.append(response.url)
                    return items[: source.max_items], "feed-common", discovered_feeds, list(source.sitemap_urls)
            except Exception:
                continue

    listing_items = parse_html_listing(home_html, homepage.url)
    recent_listing = [item for item in listing_items if _is_recent(item.get("published_at"), max_age_days)]
    if recent_listing:
        return recent_listing[: source.max_items], "html-listing", discovered_feeds, list(source.sitemap_urls)

    discovered_sitemaps = list(source.sitemap_urls)
    try:
        robots_url = urljoin(homepage.url, "/robots.txt")
        robots = client.get(robots_url, source.request_delay_seconds)
        discovered_sitemaps.extend(discover_sitemap_links(robots.text, homepage.url))
    except Exception:
        pass
    if not discovered_sitemaps:
        discovered_sitemaps.append(urljoin(homepage.url, "/sitemap.xml"))
    discovered_sitemaps = list(dict.fromkeys(discovered_sitemaps))

    sitemap_urls: list[dict] = []
    for sitemap_url in discovered_sitemaps[:4]:
        try:
            response = client.get(sitemap_url, source.request_delay_seconds)
            kind, entries = parse_sitemap(response.text)
            if kind == "index":
                recent_indexes = sorted(
                    entries,
                    key=lambda entry: entry.get("lastmod") or "",
                    reverse=True,
                )[:4]
                for index_entry in recent_indexes:
                    try:
                        child = client.get(index_entry["url"], source.request_delay_seconds)
                        child_kind, child_entries = parse_sitemap(child.text)
                        if child_kind == "urls":
                            sitemap_urls.extend(child_entries)
                    except Exception:
                        continue
            elif kind == "urls":
                sitemap_urls.extend(entries)
        except Exception:
            continue

    recent_urls = [entry for entry in sitemap_urls if _is_recent(entry.get("lastmod"), max_age_days)]
    recent_urls.sort(key=lambda entry: entry.get("lastmod") or "", reverse=True)
    enriched: list[dict] = []
    for entry in recent_urls[: min(source.max_items, 12)]:
        try:
            response = client.get(entry["url"], source.request_delay_seconds)
            metadata = parse_article_metadata(response.text, response.url)
            if not metadata.get("published_at"):
                metadata["published_at"] = entry.get("lastmod")
                metadata["date_source"] = "sitemap_lastmod"
                metadata["date_confidence"] = "low"
            enriched.append(metadata)
        except Exception:
            continue
    if enriched:
        return enriched, "sitemap", discovered_feeds, discovered_sitemaps

    return [], "none", discovered_feeds, discovered_sitemaps
