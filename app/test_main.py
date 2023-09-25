from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_repeating_symbol() -> None:
    assert is_isogram("Cook") is False


def test_higher_symbol() -> None:
    assert is_isogram("Mom") is False


def test_right() -> None:
    assert is_isogram("symbol") is True
