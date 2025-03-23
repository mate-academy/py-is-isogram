import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "",             # empty string
        "a",            # single character
        "ab",           # two different letters
        "playgrounds",  # all unique letters
        "Python",       # mixed case
    ]
)
def test_returns_true_for_valid_isograms(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",    # repeated 'o'
        "Adam",    # repeated 'a' (case-insensitive)
        "letter",  # repeated 't' and 'e'
        "AbBa",    # repeated 'b' and 'a' (case-insensitive)
        "hello",   # repeated 'l'
        "aAa",     # repeated 'a' (case-insensitive)
        "ZooM",    # repeated 'o'
    ]
)
def test_returns_false_for_non_isograms(word: str) -> None:
    assert is_isogram(word) is False
