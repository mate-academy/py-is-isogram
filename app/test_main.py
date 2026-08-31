import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("Aa", False),
    ("pp", False),
    ("p", True),
    ("", True)
], ids=["has no repeating",
        "has repeating",
        "case insensitive",
        "mixed case repeat",
        "lowercase repeat",
        "single letter",
        "empty string"])
def test_words(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
