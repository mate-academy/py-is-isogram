import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("mojo", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "isogram has no repeating letters",
        "consecutive letters are not an isogram",
        "not only consecutive letters are not an isogram",
        "string with different cases of the same letter is not an isogram",
        "empty string is an isogram"
    ]
)
def test_is_isogram_works_correctly(word: str, result: bool) -> None:
    assert is_isogram(word) == result
