import pytest
import app.main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),                  # Empty string is an isogram
        ("a", True),                 # Single lowercase letter
        ("Z", True),                 # Single uppercase letter
        ("playgrounds", True),       # Long isogram, all lowercase
        ("Subdermatoglyphic", True),  # Long isogram, mixed case
        ("look", False),             # Consecutive repeating letters
        ("aba", False),              # Non-consecutive repeating letters
        ("Adam", False),             # Mixed case repeating letters (A and a)
        ("Alphabet", False),         # Mixed case repeating letters (A and a)
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert app.main.is_isogram(word) == expected
