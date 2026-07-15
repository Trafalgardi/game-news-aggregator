from pathlib import Path

from game_news.parsers import parse_feed, parse_sitemap

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_feed() -> None:
    items = parse_feed((FIXTURES / "rss.xml").read_text(encoding="utf-8"))
    assert len(items) == 1
    assert items[0]["title"] == "Unity mobile performance update"
    assert items[0]["published_at"] == "2026-07-15T08:00:00Z"
    assert "rendering improvements" in items[0]["summary"]


def test_parse_sitemap() -> None:
    kind, entries = parse_sitemap((FIXTURES / "sitemap.xml").read_text(encoding="utf-8"))
    assert kind == "urls"
    assert len(entries) == 2
    assert entries[0]["url"] == "https://example.com/news/one"
