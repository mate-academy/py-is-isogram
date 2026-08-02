import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("Python", True),
    ("Case", True),
    ("abcdefg", True),
    ("aabbcc", False),
    ("Abcdefg", True),
    ("123", True),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
