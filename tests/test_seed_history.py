from pathlib import Path

from game_news.storage import load_articles


def test_seed_history_contains_telegram_urls() -> None:
    root = Path(__file__).resolve().parents[1]
    articles = load_articles(root / "data/articles.jsonl")
    telegram_articles = [article for article in articles if article.origin == "telegram_import"]

    assert len(telegram_articles) == 1183
    assert len(articles) >= len(telegram_articles)
    assert all(article.canonical_url.startswith("http") for article in articles)
    assert all(article.telegram_post for article in telegram_articles)
