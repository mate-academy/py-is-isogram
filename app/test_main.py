import pytest


from app.main import is_isogram


def test_returns_bool() -> None:
    assert isinstance(is_isogram("hello"), bool)


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_char_is_isogram() -> None:
    assert is_isogram("a") is True


def test_uppercase_duplicate_is_not_isogram() -> None:
    assert is_isogram("Adam") is False


def test_mixed_case_no_duplicates_is_isogram() -> None:
    assert is_isogram("Horn") is True


@pytest.mark.parametrize("word", [
    "playgrounds",
    "subdermatoglyphic",
    "ambidextrously",
    "background",
])
def test_valid_isograms(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize("word", [
    "look",
    "Adam",
    "hello",
    "eleven",
])
def test_invalid_isograms(word: str) -> None:
    assert is_isogram(word) is False
