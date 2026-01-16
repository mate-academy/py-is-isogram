import pytest

from app.main import is_isogram


def test_empty_string_is_an_isogram() -> None:
    assert is_isogram(""), "Empty string should be considered an isogram"


@pytest.mark.parametrize(
    "word,expected",
    [
        ("a", True),
        ("A", True),
        ("bad", True),
        ("BAD", True),
        ("bAd", True),
        ("awesome", False),
        ("awesomE", False),
        ("AWESOME", False),
        ("good", False),
        ("gOOd", False),
    ]
)
def test_should_be_case_insensitive(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected, (
        "Must be case insensitive('A' and 'a' are considered the same letter)"
    )


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "adam",
        "will",
        "book",
        "sixteen",
        "sensitive",
        "deprecated",
        "perseverance",
    ]
)
def test_result_for_words_with_repeating_letters_should_be_false(
    word: str
) -> None:
    assert is_isogram(word) is False, (
        "Words with repeating letters are not isograms"
    )


@pytest.mark.parametrize(
    "word",
    [
        "isogram",
        "lucrative",
        "word",
        "custom",
        "playground",
        "country",
        "roads",
        "take",
        "me",
        "home",
    ]
)
def test_result_for_words_with_unique_letters_should_be_true(
    word: str
) -> None:
    assert is_isogram(word) is True, (
        "Words with no repeating letters are isograms"
    )
