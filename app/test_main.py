import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),         # all unique letters
    ("look", False),               # repeated 'o'
    ("Adam", False),               # repeated 'a' (case-insensitive)
    ("", True),                    # empty string is an isogram
    ("Isogram", True),             # mixed case, no repeats
    ("Alphabet", False),           # repeated 'a'
    ("Dermatoglyphics", True),     # long isogram
    ("moOse", False),              # repeated 'o' with case difference
    ("Subdermatoglyphic", True),   # longest English isogram
    ("aAaAaA", False),             # all same letter, different cases
])
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
