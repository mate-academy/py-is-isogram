import pytest
from typing import Type

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("look", False),
        ("Adam", False),
        ("playgrounds", True)
    ],
    ids=[
        "empty string should return True",
        "if letter is repeated should return False",
        "function should be case-insensitive ((M and m are considered the same letter)",
        "If the letters are not repeated should return True"
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word=word) == expected_result
