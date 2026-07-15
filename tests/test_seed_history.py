from pathlib import Path

from game_news.storage import load_articles


def test_seed_history_contains_telegram_urls() -> None:
    root = Path(__file__).resolve().parents[1]
    articles = load_articles(root / "data/articles.jsonl")
    assert len(articles) == 1183
    assert all(article.canonical_url.startswith("http") for article in articles)
    assert any(article.telegram_post for article in articles)
