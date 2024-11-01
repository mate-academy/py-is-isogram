import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),  # example with all unique letters
        ("look", False),        # repeated "o"
        ("Adam", False),        # repeated "a" (case-insensitive)
        ("", True),             # empty string is an isogram
        ("isogram", True),      # all letters are unique
        ("background", True),   # all letters are unique
        ("Alphabet", False),    # repeated "a" (case-insensitive)
        ("thumbscrew", True),   # all letters are unique
        ("subdermatoglyphic", True),  # longest English isogram
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
