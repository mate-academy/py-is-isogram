from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ( "", True),
])
def test_is_isogram_examples(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected, f"Expected {expected} for '{word}', but got {is_isogram(word)}"

@pytest.mark.parametrize("word, expected", [
    ("a", True),
    ("Aa", False),
    ("abcda", False),
    ("AbCd", True),
    ("aaa", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
])
def test_is_isogram_boundaries(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected, f"Expected {expected} for '{word}', but got {is_isogram(word)}"
