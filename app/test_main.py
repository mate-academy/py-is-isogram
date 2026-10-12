
import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("is", True),
        ("playgrounds", True),
        ("background", True),
        ("look", False),
        ("letter", False),
        ("Adam", False),
        ("Alphabet", False),
        ("hello", False),
        ("Python", True),
        ("Aa", False),
        ("aA", False),
        ("abcde", True),
        ("abcdea", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
