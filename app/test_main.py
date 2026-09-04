import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("A", True),
        ("Aa", False),
        ("abcde", True),
        ("abca", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
