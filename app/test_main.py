import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),    # all unique letters
        ("look", False),          # repeating 'o'
        ("Adam", False),          # 'a' repeats (case-insensitive)
        ("", True),               # empty string isogram
        ("isogram", True),        # all unique
        ("Alphabet", False),      # repeating 'a' (case-insensitive)
        ("Aa", False),            # same letter different case
        ("m", True),              # single letter
        ("abca", False),          # repeating 'a'
        ("Dermatoglyphics", True),  # famous isogram example
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
