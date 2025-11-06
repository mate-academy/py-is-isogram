# app/test_main.py

import pytest
from app.main import is_isogram

@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("Isogram", True),
    ("Alphabet", False),
    ("Dermatoglyphics", True),
    ("moOse", False),
    ("Subdermatoglyphic", True),
    ("aAaAaA", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
