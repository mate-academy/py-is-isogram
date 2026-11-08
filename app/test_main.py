import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("", True),
        ("look", False),
        ("Adam", False),
        ("Alphabet", False),
        ("isograms", False),
    ],
    ids=[
        "word without repeated letters is an isogram",
        "empty string is an isogram",
        "consecutive repeated letters are not an isogram",
        "check is case-insensitive",
        "repeated letters in different cases are not an isogram",
        "non-consecutive repeated letters are not an isogram",
    ]
)
def test_should_check_if_word_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
