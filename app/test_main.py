import pytest
from app.main import is_isogram
from typing import List, Tuple

@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("subdermatoglyphic", True),
    ("Alphabet", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected

def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Sponge") == True
    assert is_isogram("sPoNgE") == True

def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") == True
