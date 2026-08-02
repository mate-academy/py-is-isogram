from app.main import is_isogram
from typing import Any
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Aa", False),
        ("A", True),
        ("11", False),
        ("12", True),
    ])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        (None),
        (1),
        (1.0),
        ([1]),
        (["1"]),
        ({1}),
    ])
def test_invalid_word_input(word: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
