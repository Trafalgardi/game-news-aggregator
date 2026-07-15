from pathlib import Path

from game_news.config import load_config, validate_config


def test_repository_config_is_valid() -> None:
    root = Path(__file__).resolve().parents[1]
    config = load_config(root / "config/sources.yaml", root / "config/keywords.yaml")
    assert len(config.sources) == 92
    assert sum(source.enabled for source in config.sources) == 30
    assert validate_config(config) == []
