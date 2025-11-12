from app.main import is_isogram


def test_empty_string_returns_true() -> None:
    assert is_isogram("") is True


def test_two_non_consecutive_repeating_letters_returns_false() -> None:
    assert is_isogram("Adam") is False


def test_two_consecutive_repeating_letters_returns_false() -> None:
    assert is_isogram("look") is False


def test_no_repeating_letters_returns_true() -> None:
    assert is_isogram("playgrounds") is True
