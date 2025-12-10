from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, excepted",
    [
        ("", True),
        (" ", True),
        ("B", True),
        ("aaaaaaaa", False),
        ("325790", True),
        ("   ", False),
        ("aA", False),
        ("kara", False)
    ],
    ids=[
        "empty string is isogram",
        "one space is isogram",
        "one letter is isogram",
        "several identical letters are isogram",
        "string with different numbers is isogram",
        "string with several spaces is not isogram",
        "two letters in different cases are not isogram",
        "not only consecutive letters are not isogram"
    ]
)
def test_is_isogram(word: str, excepted: bool) -> None:
    assert is_isogram(word) is excepted
