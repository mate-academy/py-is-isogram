import pytest

from app import main


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_singlr_letter_is_isogram() -> None:
    assert main.is_isogram("a") is True


@pytest.mark.parametrize(
    "word",
    [
        "playgrounds",
        "isogram",
        "background",
        "abc",
        "ab",
    ],
)
def test_words_without_repeated_letters_are_isograms(word: str) -> None:
    assert main.is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "aa",
        "letter",
        "success",
    ],
)
def test_words_with_consecutive_repeated_letters_are_not_isograms(
    word: str
) -> None:
    assert main.is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    [
        "tenet",
        "abca",
        "abcdefga",
        "banana",
    ],
)
def test_words_with_non_consecutive_repeated_letters_are_not_isograms(
    word: str
) -> None:
    assert main.is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    [
        "Adam",
        "aA",
        "Aa",
        "AbcB",
        "LOok",
    ],
)
def test_function_is_case_insensitive_for_repeated_letters(word: str) -> None:
    assert main.is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    [
        "PlayGrounds",
        "ISOGRAM",
        "AbC",
    ],
)
def test_isograms_with_uppercase_letters(word: str) -> None:
    assert main.is_isogram(word) is True


def test_function_returns_boolean() -> None:
    assert isinstance(main.is_isogram("abc"), bool)
    assert isinstance(main.is_isogram("aab"), bool)
