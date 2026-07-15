from game_news.normalize import normalize_url, normalized_title, stable_id


def test_normalize_url_removes_tracking_and_www() -> None:
    value = normalize_url("http://www.Example.com/a//b/?utm_source=x&b=2&a=1#fragment")
    assert value == "https://example.com/a/b?a=1&b=2"


def test_normalized_title_is_comparable() -> None:
    assert normalized_title("Unity: Performance — Update!") == "unity performance update"


def test_stable_id_is_deterministic() -> None:
    assert stable_id("x") == stable_id("x")
    assert stable_id("x") != stable_id("y")
