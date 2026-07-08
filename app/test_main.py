import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("aA", False),
    ],
    ids=[
        "all unique letters is an isogram",
        "consecutive repeated letters is not an isogram",
        "case-insensitive repeated letter is not an isogram",
        "empty string is an isogram",
        "single letter is an isogram",
        "same letter in different case counted once",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
