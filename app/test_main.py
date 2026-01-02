import pytest
from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_simple_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_simple_non_isogram() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_isogram() -> None:
    assert is_isogram("Machine") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("abc", True),
        ("aba", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
        ("subdermatoglyphic", True),
    ]
)
def test_various_words(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
