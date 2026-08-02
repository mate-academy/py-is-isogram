from app.main import is_isogram

from typing import Any

import pytest


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("DERBY", True),
    ("Alphabet", False)
])
def test_is_isogram(word: Any, expected: float) -> None:
    assert is_isogram(word) == expected
