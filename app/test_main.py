import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),                # empty string is an isogram
        ("playgrounds", True),     # all letters unique
        ("look", False),           # double 'o'
        ("Adam", False),           # case-insensitive: A == a
        ("isogram", True),         # classic positive case
        ("letter", False),         # repeated 't'
        ("Subdermatoglyphic", True),  # known long isogram word
        ("Alphabet", False),       # case-insensitive duplicate
    ],
)
def test_is_isogram_examples_and_various_cases(
    word: str,
    expected: bool
) -> None:
    assert is_isogram(word) is expected


def test_all_single_letter_words_are_isograms() -> None:
    for ch in "abcdefghijklmnopqrstuvwxyz":
        assert is_isogram(ch)
        assert is_isogram(ch.upper())
