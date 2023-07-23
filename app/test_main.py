from typing import Any

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_outcome",
    [
        ("", True),
        ("Aaron", False),
        ("Adam", False),
        ("Antarctica", False),
        ("BBQ", False),
        ("Pyhon", True),
        ("terminal", True),
        ("reboot", False)
    ]
)
def test_should_return_correct_results(
        word: str,
        expected_outcome: bool
) -> None:
    assert is_isogram(word) == expected_outcome


@pytest.mark.parametrize(
    "word, expected_error",
    [
        (12, AttributeError),
        (True, AttributeError)
    ]
)
def test_should_raise_correct_errors(
        word: str,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
