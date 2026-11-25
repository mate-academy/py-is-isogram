from typing import Any

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("A", True),
        ("ab", True),
        ("isogram", True),
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
        ("aa", False),
        ("aA", False),
        ("Aa", False),
        ("Mm", False),
        ("look", False),
        ("Adam", False),
        ("moOn", False),
        ("aabc", False),
        ("abbc", False),
        ("abcb", False),
        ("abca", False),
        ("abcdefghijklmnopqrstuvwxyza", False),
        ("ab" * 5000, False),
    ],
)
def test_should_check_whether_word_is_isogram(
    word: str,
    expected: bool,
) -> None:
    assert is_isogram(word) is expected


@pytest.mark.parametrize(
    "word",
    [10, None, ["a", "b"]],
)
def test_should_raise_error_for_incorrect_types(word: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
