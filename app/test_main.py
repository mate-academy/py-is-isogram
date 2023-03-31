from app.main import is_isogram


def test_no_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_no_consecutive_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_no_repeating_letters_with_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True
