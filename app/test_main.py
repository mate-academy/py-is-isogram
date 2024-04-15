import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_word, result",
    [
        ("", True),
        ("AalL", False),
        ("abcda", False),
        ("Abcdzx", True),
        ("efg", True),
    ],
    ids=[
        "test empty string",
        "test two repeating letters with upper-case",
        "test one repeating letter with lower-case and non-consecutive",
        "test no repeating letters with upper-case",
        "test no repeating letters with lower-case"
    ]
)
def test_letters_for_isogram(test_word: str, result: bool):
    assert is_isogram(test_word) == result
