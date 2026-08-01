import pytest
from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True, "Empty string should be an isogram"


@pytest.mark.parametrize("word", [
    "playgrounds",
    "Python",
    "isogram",
    "Quiz",
])
def test_valid_isograms(word: str) -> None:
    assert is_isogram(word) is True, f"{word} should be an isogram"


@pytest.mark.parametrize("word", [
    "look",
    "Adam",
    "letter",
    "Balloon",
])
def test_non_isograms(word: str) -> None:
    assert is_isogram(word) is False, f"{word} should not be an isogram"


def test_case_insensitivity() -> None:
    assert is_isogram("Aa") is False, "Function should be case-insensitive"


def test_single_letter_words() -> None:
    for letter in "abcdefghijklmnopqrstuvwxyz":
        assert is_isogram(letter) is True, (
            f"Single letter {letter} should be an isogram"
        )
