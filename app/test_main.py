import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),                     # Empty string
    ("playgrounds", True),         # All unique letters
    ("look", False),               # Repeated 'o'
    ("Adam", False),               # Case-insensitive check: 'a' and 'A'
    ("subdermatoglyphic", True),   # Known long isogram
    ("Alphabet", False),           # Repeated 'a'
    ("Dermatoglyphics", True),     # Case-insensitive unique letters
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
