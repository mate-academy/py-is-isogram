import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("look", False),
        ("Adam", False),
        ("moOse", False),
    ],
    ids=[
        "empty string is an isogram",
        "single letter is an isogram",
        "word with unique letters is an isogram",
        "word with unique letters in different cases is an isogram",
        "word with consecutive repeated letters is not an isogram",
        "word with non-consecutive repeated letters is not an isogram",
        "repeated letters are case-insensitive",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
