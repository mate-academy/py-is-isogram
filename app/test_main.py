from typing import Any

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("word", True),
        ("wword", False),
        ("wowrd", False),
        ("Wword", False),
        ("", True),
        ("Hi\nworld\n!", False)
    ]
)
def test_values(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result


@pytest.mark.parametrize(
    "word,expected_error",
    [
        (int(), AttributeError),
        (set(), AttributeError),
        (dict(), AttributeError),
        (tuple(), AttributeError),
        (complex(), AttributeError),
    ]
)
def test_exceptions(
        word: Any,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
