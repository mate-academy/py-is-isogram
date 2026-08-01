import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word,expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("Aa", False),
    ("aA", False),
    ("abcdeFghIjklmnOpqrStuvWxYz", True),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_single_letter() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_repeated_letters_in_long_word() -> None:
    assert is_isogram("subdermatoglyphic") is True
    assert is_isogram("alphabet") is False
