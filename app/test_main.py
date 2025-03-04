from __future__ import annotations

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("playgrounds", True),
        ("A", True),
        ("look", False),
        ("Adam", False),
    ],
    ids=[
        "empty string is an isogram",
        "'playgrounds' is an isogram",
        "1 char in string is an isogram",
        "'look' isn't an isogram",
        "function should be case-insensitive"
    ]
)
def test_general(word: str, result: bool) -> None:
    assert is_isogram(word) == result
