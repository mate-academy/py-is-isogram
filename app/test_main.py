import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),  # Standard isogram
        ("look", False),         # Consecutive repeating letters
        ("Adam", False),         # Case-insensitive repeating letters (A and a)
        ("", True),               # Empty string edge case
        ("alphabet", False),      # Non-consecutive repeating letters
        ("isogram", True),       # Another standard isogram
        ("ABCdef", True),        # Mixed case isogram
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
