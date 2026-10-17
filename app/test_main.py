import pytest

from app.main import is_isogram


def test_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True


@pytest.mark.parametrize("word", ["a", "Z"])
def test_single_letter_is_an_isogram(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "playgrounds",
        "abcdefghijklmnopqrstuvwxyz",
        "BACKGROUND",
        "AbCdEf",
    ],
)
def test_word_without_repeated_letters_is_an_isogram(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize("word", ["aa", "look", "HELLO"])
def test_consecutive_repeated_letters_are_not_an_isogram(
    word: str,
) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize("word", ["abca", "radar", "ABCDB"])
def test_non_consecutive_repeated_letters_are_not_an_isogram(
    word: str,
) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize("word", ["Aa", "aA", "Adam", "abCB"])
def test_repeated_letters_in_different_cases_are_not_an_isogram(
    word: str,
) -> None:
    assert is_isogram(word) is False
