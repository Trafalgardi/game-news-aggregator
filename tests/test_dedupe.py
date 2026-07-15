from game_news.dedupe import cluster_articles
from game_news.models import Article


def make_article(article_id: str, title: str, source: str, score: int) -> Article:
    return Article(
        id=article_id,
        url=f"https://{source}.example/{article_id}",
        canonical_url=f"https://{source}.example/{article_id}",
        title=title,
        source_id=source,
        source_name=source,
        source_domain=f"{source}.example",
        source_category="industry_media",
        source_priority=80,
        published_at="2026-07-15T10:00:00Z",
        discovered_at="2026-07-15T11:00:00Z",
        date_source="feed",
        date_confidence="high",
        importance_score=score,
    )


def test_cluster_articles_keeps_best_primary() -> None:
    low = make_article("a", "Unity announces a new mobile performance tool", "low", 60)
    high = make_article("b", "Unity announces new mobile performance tools", "high", 90)
    result = cluster_articles([low, high], threshold=85)
    assert len(result) == 1
    assert result[0].id == "b"
    assert low.duplicate_of == "b"
    assert low.url in result[0].duplicate_urls
