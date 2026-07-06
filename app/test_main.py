import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word,expected", [
    ("", True),
    ("A", True),
    ("a", True),
    ("playgrounds", True),
    ("Playgrounds", True),
])
def test_is_isogram_true(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("look", False),
    ("Adam", False),
    ("Aa", False),
    ("aabbcc", False),
])
def test_is_isogram_false(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
