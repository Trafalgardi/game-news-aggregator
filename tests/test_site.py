from pathlib import Path

from game_news.site import build_site


def test_build_site(tmp_path: Path) -> None:
    output = build_site(tmp_path)
    assert output.exists()
    text = output.read_text(encoding="utf-8")
    assert "latest.json" in text
    assert "Game News Intelligence" in text
