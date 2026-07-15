from pathlib import Path

from game_news.storage import load_articles
from game_news.telegram_import import import_telegram_export

FIXTURES = Path(__file__).parent / "fixtures"


def test_import_telegram_extracts_visible_and_hidden_links(tmp_path: Path) -> None:
    output = tmp_path / "articles.jsonl"
    total, added = import_telegram_export(FIXTURES / "telegram_export.json", output)
    articles = load_articles(output)
    assert total == 2
    assert added == 2
    assert len(articles) == 2
    urls = {article.canonical_url for article in articles}
    assert "https://example.com/article" in urls
    assert "https://other.example/news" in urls
