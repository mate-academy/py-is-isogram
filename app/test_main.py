from app.main import is_isogram


def test_is_isogram_non_repeating() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_cons_repeating() -> None:
    assert is_isogram("look") is False


def test_is_isogram_non_cons_repeating() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True
