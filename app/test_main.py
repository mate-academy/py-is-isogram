import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),       # consecutive duplicate letters
        ("Adam", False),       # case-insensitive check
        ("", True),            # empty string is isogram
        ("isogram", True),
        ("Alphabet", False),   # repeated letter in different case
        ("abc", True),
        ("aba", False),        # non-consecutive duplicate letters
        ("aabb", False),       # consecutive duplicate letters
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
