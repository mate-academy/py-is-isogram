import pytest
from typing import Any

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("isogram", True),
        ("isIsogram", False),
        ("hello", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("aba", False),
        ("moOse", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        123,
        None,
        ["list"],
        {"set"},
        ("tuple",),
    ],
)
def test_is_isogram_invalid_input(word: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
