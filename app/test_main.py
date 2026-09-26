import pytest
from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_lowercase_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_repeating_consecutive_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


@pytest.mark.parametrize(
    "word, expected",
    [
        ("a", True),
        ("abcdefg", True),
        ("aba", False),
        ("moOse", False),
        ("isogram", True),
        ("Alphabet", False),
    ],
)
def test_is_isogram_various_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
