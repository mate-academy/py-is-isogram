from app import main

import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("lamp", True),
        ("hello", False),
        ("Lamp", True),
        ("Hello", False),
        ("a", True),
        ("", True),
        ("aA", False),
        ("Adam", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
