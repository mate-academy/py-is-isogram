from typing import Any

from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "playgrounds is isogram",
        "look has repeating letters",
        "Adam has repeating letters",
        "Empty string is isogram",
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word, expected_error",
    [
        pytest.param(12, AttributeError),
    ]
)
def test_is_isogram_for_errors(word: str, expected_error: Any) -> None:
    with pytest.raises(expected_error):
        assert is_isogram(word)
