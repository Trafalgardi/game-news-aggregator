from __future__ import annotations

from datetime import UTC, datetime, timedelta

from rapidfuzz.fuzz import ratio

from game_news.models import Article
from game_news.normalize import normalized_title
from game_news.parsers import parse_datetime


def titles_similar(left: str, right: str, threshold: int) -> bool:
    a = normalized_title(left)
    b = normalized_title(right)
    if not a or not b:
        return False
    if a == b:
        return True
    return ratio(a, b) >= threshold


def _date(article: Article) -> datetime:
    return parse_datetime(article.published_at) or parse_datetime(article.discovered_at) or datetime.now(UTC)


def cluster_articles(articles: list[Article], threshold: int = 92) -> list[Article]:
    ordered = sorted(
        articles,
        key=lambda article: (article.importance_score, article.source_priority, _date(article)),
        reverse=True,
    )
    primaries: list[Article] = []
    for article in ordered:
        match: Article | None = None
        article_date = _date(article)
        for primary in primaries:
            if abs(article_date - _date(primary)) > timedelta(hours=72):
                continue
            if titles_similar(article.title, primary.title, threshold):
                match = primary
                break
        if match is None:
            primaries.append(article)
            continue
        article.duplicate_of = match.id
        if article.url not in match.duplicate_urls:
            match.duplicate_urls.append(article.url)
        if article.source_name not in match.duplicate_sources:
            match.duplicate_sources.append(article.source_name)
    return sorted(primaries, key=lambda article: (_date(article), article.importance_score), reverse=True)
