import pytest
from app.main import is_isogram

@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),     # True case with no repeating letters
    ("look", False),           # False case with repeating 'o'
    ("Adam", False),           # False case with case-insensitive repeat 'a'
    ("", True),                # True case for empty string
    ("background", True),      # True case with longer word
    ("aA", False),             # False case for case-insensitivity in short word
    ("dermatoglyphics", True), # True case for longer word with no repeating letters
    ("consecutive", False),    # False case with multiple repeats
    ("Subdermatoglyphic", True), # True case with long word and mixed casing
    ("Alphabet", False)        # False case with repeating 'a' in mixed casing
])
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected, f"Expected {expected} for word '{word}'"