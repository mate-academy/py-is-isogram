from app import main


def test_isogram_returns_true() -> None:
    assert main.is_isogram("playgrounds") is True


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_isogram_is_case_insensitive() -> None:
    assert main.is_isogram("Adam") is False


def test_consecutive_repeated_letters_not_isogram() -> None:
    assert main.is_isogram("look") is False


def test_non_consecutive_repeated_letters_not_isogram() -> None:
    assert main.is_isogram("abca") is False
