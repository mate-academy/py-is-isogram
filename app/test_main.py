import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ["", True],
        ["  ", False],
        ["Expect", False],
        ["AdAm", False],
        ["abca", False],
        ["plane", True],
        ["@#$!^&", True],
        ["@#$@!^&", False],
    ],
    ids=[
        "empty string",
        "two spacelines",
        "same letter in different cases",
        "same letter in upper case",
        "same letter in lower case",
        "doesnt contain repeating letters",
        "contain special symbols",
        "contain repeating special symbols",
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
