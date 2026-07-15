from __future__ import annotations

from typing import Any

from game_news.normalize import normalized_title


def classify_and_score(
    title: str,
    summary: str,
    source_priority: int,
    source_tags: list[str],
    topics: dict[str, dict[str, Any]],
    date_confidence: str,
) -> tuple[list[str], int]:
    haystack = normalized_title(f"{title} {summary}")
    matched: list[str] = []
    keyword_score = 0
    for topic_id, topic in topics.items():
        keywords = [normalized_title(str(value)) for value in topic.get("keywords", [])]
        matches = sum(1 for keyword in keywords if keyword and keyword in haystack)
        if matches:
            matched.append(topic_id)
            keyword_score += min(int(topic.get("weight", 8)) * matches, 24)

    tag_bonus = min(len(source_tags) * 2, 8)
    confidence_bonus = {"high": 8, "medium": 4, "low": 1, "none": -8}.get(date_confidence, 0)
    score = round(source_priority * 0.55 + keyword_score + tag_bonus + confidence_bonus)
    return matched, max(0, min(100, score))
