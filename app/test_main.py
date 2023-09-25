from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("aasdfg", False),
        ("eleven", False),
        ("subdermatoglyphic", True),
        ("Alphabet", False),
    ],
    ids=[
        "test empty string",
        "test non-consecutive repeating letters",
        "test consecutive repeating letters",
        "test non-consecutive without repeating letters",
        "test word with the same letter with different case"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
