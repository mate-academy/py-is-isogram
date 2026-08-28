import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Aa", False),
        ("abc", True),
        ("abca", False),
        ("abcdefga", False),
        ("Python", True),
        ("Pythonp", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
