from app import main


def test_isogram_returns_true() -> None:
    assert main.is_isogram("playgrounds") is True


def test_non_isogram_consecutive_letters() -> None:
    assert main.is_isogram("look") is False


def test_non_isogram_non_consecutive_letters() -> None:
    assert main.is_isogram("abca") is False


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_case_insensitive_same_letter() -> None:
    assert main.is_isogram("Adam") is False


def test_case_insensitive_isogram() -> None:
    assert main.is_isogram("Lingo") is True


def test_single_character_is_isogram() -> None:
    assert main.is_isogram("a") is True
