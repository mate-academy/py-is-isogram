import pytest
from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("adam", False),
        ("", True),
        ("a", True),
        ("isogram", True),
        ("Cheese", False),
        ("Shelf", True),
        ("Aa", False),
    ],
    ids=[
        "uniq",
        "repeat",
        "empty string",
        "single letter",
        "classic isogram",
        "case insensitive, repeat",
        "case insensitive, uniq",
        "case insensitive, two letters, repeat",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
