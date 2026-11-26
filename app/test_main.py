import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Python", True),
        ("Friend", True),
        ("look", False),
        ("Adam", False),
        ("System", False),
        ("Bool", False),
        ("aa", False),
        ("Aa", False),
        ("aba", False),
        ("abca", False),
        ("abcdea", False),
        ("abBc", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
