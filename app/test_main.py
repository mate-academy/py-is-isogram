import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("abcdABCD", False),
        ("abcdefghijklmn", True),
        ("aabbcc", False)
    ],
    ids=[
        "empty string is isogram",
        "case_insensitive_non_consecutive_not_isogram",
        "string_is_isogram",
        "consecutive_letters_not_isogram"
    ]
)
def test_check_isogram_correctly(word: str, result: bool) -> None:
    assert is_isogram(word) == result
