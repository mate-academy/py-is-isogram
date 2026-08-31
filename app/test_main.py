import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        # Empty string (should be True)
        ("", True),
        # Single character string
        ("a", True),
        # Valid isograms with all lowercase letters
        ("playgrounds", True),
        ("subdermatoglyphic", True),
        # Words with repeating non-consecutive letters
        ("look", False),
        ("geese", False),
        # Case-insensitive checks (e.g., 'A' and 'a', 'M' and 'm')
        ("Adam", False),
        ("Alphabet", False),
        # Mixed-case valid isograms
        ("Dermatoglyphics", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
