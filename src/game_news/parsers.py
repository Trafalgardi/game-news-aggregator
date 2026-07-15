from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections.abc import Iterable
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urljoin

import feedparser
from bs4 import BeautifulSoup
from dateutil import parser as date_parser

from game_news.normalize import normalize_whitespace, title_from_url

RSS_TYPES = {
    "application/rss+xml",
    "application/atom+xml",
    "application/rdf+xml",
    "application/xml",
    "text/xml",
}


def parse_datetime(value: Any) -> datetime | None:
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, (int, float)):
        dt = datetime.fromtimestamp(value, tz=UTC)
    else:
        text = normalize_whitespace(str(value))
        if not text:
            return None
        try:
            dt = date_parser.parse(text)
        except (ValueError, TypeError, OverflowError):
            try:
                dt = parsedate_to_datetime(text)
            except (ValueError, TypeError, OverflowError):
                return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def iso_utc(value: datetime | None) -> str | None:
    if value is None:
        return None
    return value.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def discover_feed_links(html_text: str, base_url: str) -> list[str]:
    soup = BeautifulSoup(html_text, "lxml")
    links: list[str] = []
    for tag in soup.find_all("link", href=True):
        rel = {str(item).lower() for item in tag.get("rel", [])}
        type_value = str(tag.get("type", "")).lower()
        if "alternate" in rel and (type_value in RSS_TYPES or "rss" in type_value or "atom" in type_value):
            links.append(urljoin(base_url, tag["href"]))
    return list(dict.fromkeys(links))


def discover_sitemap_links(robots_text: str, base_url: str) -> list[str]:
    values: list[str] = []
    for line in robots_text.splitlines():
        if line.lower().startswith("sitemap:"):
            value = line.split(":", 1)[1].strip()
            if value:
                values.append(urljoin(base_url, value))
    return list(dict.fromkeys(values))


def parse_feed(xml_text: str) -> list[dict[str, Any]]:
    parsed = feedparser.parse(xml_text)
    items: list[dict[str, Any]] = []
    for entry in parsed.entries:
        link = entry.get("link") or entry.get("id")
        if not link:
            continue
        published = (
            parse_datetime(entry.get("published"))
            or parse_datetime(entry.get("updated"))
            or parse_datetime(entry.get("created"))
        )
        summary = entry.get("summary") or entry.get("description") or ""
        soup = BeautifulSoup(str(summary), "lxml")
        items.append(
            {
                "url": str(link),
                "title": normalize_whitespace(str(entry.get("title") or title_from_url(str(link)))),
                "summary": normalize_whitespace(soup.get_text(" ", strip=True)),
                "author": normalize_whitespace(str(entry.get("author") or "")),
                "published_at": iso_utc(published),
                "date_source": "feed",
                "date_confidence": "high" if published else "none",
            }
        )
    return items


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def parse_sitemap(xml_text: str) -> tuple[str, list[dict[str, Any]]]:
    root = ET.fromstring(xml_text)
    kind = _local_name(root.tag)
    entries: list[dict[str, Any]] = []
    if kind == "sitemapindex":
        for node in root:
            if _local_name(node.tag) != "sitemap":
                continue
            values = {_local_name(child.tag): (child.text or "").strip() for child in node}
            if values.get("loc"):
                entries.append(
                    {
                        "url": values["loc"],
                        "lastmod": iso_utc(parse_datetime(values.get("lastmod"))),
                    }
                )
        return "index", entries

    if kind == "urlset":
        for node in root:
            if _local_name(node.tag) != "url":
                continue
            values = {_local_name(child.tag): (child.text or "").strip() for child in node}
            if values.get("loc"):
                entries.append(
                    {
                        "url": values["loc"],
                        "lastmod": iso_utc(parse_datetime(values.get("lastmod"))),
                    }
                )
        return "urls", entries

    return "unknown", []


def _iter_json_ld(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        graph = value.get("@graph")
        if isinstance(graph, list):
            for item in graph:
                yield from _iter_json_ld(item)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_json_ld(item)


def _json_ld_url(item: dict[str, Any]) -> str | None:
    raw = item.get("url") or item.get("mainEntityOfPage")
    if isinstance(raw, dict):
        raw = raw.get("@id") or raw.get("url")
    return str(raw) if raw else None


def parse_html_listing(html_text: str, base_url: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(html_text, "lxml")
    items: list[dict[str, Any]] = []

    for script in soup.find_all("script", attrs={"type": re.compile("ld\\+json", re.I)}):
        try:
            data = json.loads(script.string or script.get_text() or "null")
        except (json.JSONDecodeError, TypeError):
            continue
        for obj in _iter_json_ld(data):
            types = obj.get("@type", [])
            if isinstance(types, str):
                types = [types]
            if not any(t in {"NewsArticle", "Article", "BlogPosting"} for t in types):
                continue
            url = _json_ld_url(obj)
            if not url:
                continue
            published = parse_datetime(obj.get("datePublished") or obj.get("dateModified"))
            items.append(
                {
                    "url": urljoin(base_url, url),
                    "title": normalize_whitespace(str(obj.get("headline") or obj.get("name") or title_from_url(url))),
                    "summary": normalize_whitespace(str(obj.get("description") or "")),
                    "author": "",
                    "published_at": iso_utc(published),
                    "date_source": "json_ld",
                    "date_confidence": "high" if obj.get("datePublished") else "medium" if published else "none",
                }
            )

    for article in soup.find_all("article"):
        link_tag = article.find("a", href=True)
        if not link_tag:
            continue
        heading = article.find(["h1", "h2", "h3", "h4"]) or link_tag
        time_tag = article.find("time")
        published = None
        if time_tag:
            published = parse_datetime(time_tag.get("datetime") or time_tag.get_text(" ", strip=True))
        if not published:
            continue
        items.append(
            {
                "url": urljoin(base_url, link_tag["href"]),
                "title": normalize_whitespace(heading.get_text(" ", strip=True)),
                "summary": "",
                "author": "",
                "published_at": iso_utc(published),
                "date_source": "html_time",
                "date_confidence": "medium",
            }
        )

    unique: dict[str, dict[str, Any]] = {}
    for item in items:
        unique[item["url"]] = item
    return list(unique.values())


def parse_article_metadata(html_text: str, base_url: str) -> dict[str, Any]:
    soup = BeautifulSoup(html_text, "lxml")

    def meta(*keys: tuple[str, str]) -> str:
        for attr, value in keys:
            tag = soup.find("meta", attrs={attr: value})
            if tag and tag.get("content"):
                return normalize_whitespace(str(tag["content"]))
        return ""

    canonical_tag = soup.find("link", rel=lambda value: value and "canonical" in value)
    canonical = urljoin(base_url, canonical_tag["href"]) if canonical_tag and canonical_tag.get("href") else base_url
    title = meta(("property", "og:title"), ("name", "twitter:title"))
    if not title and soup.title:
        title = normalize_whitespace(soup.title.get_text(" ", strip=True))
    description = meta(("property", "og:description"), ("name", "description"), ("name", "twitter:description"))
    published_text = meta(
        ("property", "article:published_time"),
        ("name", "date"),
        ("name", "pubdate"),
        ("itemprop", "datePublished"),
    )
    published = parse_datetime(published_text)

    if not published or not title:
        json_ld_items = parse_html_listing(html_text, base_url)
        if json_ld_items:
            first = json_ld_items[0]
            title = title or first["title"]
            description = description or first["summary"]
            published = published or parse_datetime(first["published_at"])

    return {
        "url": canonical,
        "title": title or title_from_url(canonical),
        "summary": description,
        "author": meta(("name", "author"), ("property", "article:author")),
        "published_at": iso_utc(published),
        "date_source": "article_metadata" if published else "none",
        "date_confidence": "high" if published else "none",
    }
