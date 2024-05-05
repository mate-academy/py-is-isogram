from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("adam") is False
    assert is_isogram("AdamM") is False


def test_is_isogram_isograms() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("background") is True
    assert is_isogram("subdermatoglyphic") is True


def test_is_isogram_non_isograms() -> None:
    assert is_isogram("look") is False
    assert is_isogram("mirror") is False
    assert is_isogram("apple") is False
