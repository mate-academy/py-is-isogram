from typing import Any
from app.main import is_isogram

# write your code here

import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("AA", False),
        ("Aa", False),
        ("Test", False),
        ("playgrounds", True),
        ("a123B", True),
        ("", True),
    ]
)
def test_can_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), (f"Is isogram {word} should be equal to {result}")
