import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("aba", False),
        ("moOse", False),
    ],
    ids=[
        "empty string is isogram",
        "single character is isogram",
        "valid lowercase word without duplicates",
        "consecutive identical letters are not isogram",
        "case-insensitive duplicate at start is not isogram",
        "non-consecutive lowercase duplicate is not isogram",
        "case-insensitive duplicate in middle is not isogram",
    ],
)
def test_is_isogram(string: str, expected: bool) -> None:
    assert is_isogram(string) == expected
