import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),     # typical isogram
        ("look", False),           # repeated letter
        ("Adam", False),           # case-insensitive repetition
        ("", True),               # empty string is an isogram
        ("a", True),              # single character
        ("abcdefg", True),        # all unique letters
        ("Alphabet", False),      # repeated letters with mixed case
        ("Dermatoglyphics", True),  # classic isogram example
        ("moOse", False),         # repeated letters with different cases
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
