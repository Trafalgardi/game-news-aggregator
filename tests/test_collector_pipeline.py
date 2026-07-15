import json
from pathlib import Path

from game_news.collector import collect
from game_news.config import load_config
from game_news.models import Article, SourceResult


def test_collect_writes_public_payload(monkeypatch, tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    config = load_config(root / "config/sources.yaml", root / "config/keywords.yaml")
    source = next(item for item in config.sources if item.id == "app2top-ru")
    config.sources = [source]

    article = Article(
        id="fixture",
        url="https://example.com/fresh",
        canonical_url="https://example.com/fresh",
        title="Unity mobile performance and monetization update",
        source_id=source.id,
        source_name=source.name,
        source_domain="example.com",
        source_category=source.category,
        source_priority=source.priority,
        published_at="2099-01-01T10:00:00Z",
        discovered_at="2099-01-01T11:00:00Z",
        date_source="feed",
        date_confidence="high",
        matched_topics=["unity_engine"],
        importance_score=90,
    )
    result = SourceResult(
        source_id=source.id,
        source_name=source.name,
        status="ok",
        checked_at="2099-01-01T11:00:00Z",
        method="feed",
        fetched_count=1,
        accepted_count=1,
        new_count=1,
    )

    monkeypatch.setattr("game_news.collector._collect_source", lambda *_args: ([article], result))
    output = collect(config, tmp_path, window_hours=999999, source_ids=[source.id])

    assert output["added_count"] == 1
    latest = json.loads((tmp_path / "public/latest.json").read_text(encoding="utf-8"))
    status = json.loads((tmp_path / "public/status.json").read_text(encoding="utf-8"))
    assert latest["article_count"] == 1
    assert latest["articles"][0]["url"] == article.url
    assert status["ok"] == 1
    assert (tmp_path / "public/index.html").exists()
