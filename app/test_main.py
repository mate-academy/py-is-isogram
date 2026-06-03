import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word,expected", [
    ("", True),
    ("e", True),
    ("abc", True),
    ("look", False),
    ("adam", False),
    ("Adam", False),
    ("nnn", False),
    ("ab", True),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
