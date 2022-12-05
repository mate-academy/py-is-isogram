import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("backgrounds", True),
        ("pool", False),
        ("Check", False)
    ],
    ids=[
        "Empty string is an isogram.",
        "An isogram is a word that has no repeating letters, "
        "consecutive or non-consecutive.",
        "Not only consecutive letters are not an isogram.",
        "String with different cases of the same letter (non-consecutive) "
        "is not an isogram."
    ]
)
def test_if_word_is_isofram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
