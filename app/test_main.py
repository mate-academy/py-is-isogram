import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("BACKGROUNDS", True),
        ("", True),
        ("A", True),
        ("Adam", False),
        ("look", False)
    ],
    ids=[
        "'playgrounds' is an isogram",
        "'BACKGROUNDS' is an isogram",
        "empty string is an isogram",
        "single letter is an isogram",
        "'Adam' is an isogram",
        "'look' is an isogram"
    ]
)
def test_is_isogram_function(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
