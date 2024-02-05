import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("MooN", False),
    ("mOon", False),
    ("Moon", False),
    ("playgrounds", True),
    ("abcdefg", True),
    ("xyz", True),
    ("look", False),
    ("Adam", False),
    ("hello", False),
])
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) == expected
