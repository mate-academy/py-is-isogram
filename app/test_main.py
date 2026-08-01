from typing import Any

from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected_boolean",
    [
        pytest.param("playgrounds", True, id="test playgrounds"),
        pytest.param("look", False, id="test look"),
        pytest.param("Adam", False, id="test Adam"),
        pytest.param("", True, id="empty test")
    ]
)
def test_multiply_check(word: str, expected_boolean: bool) -> None:
    assert is_isogram(word) == expected_boolean


@pytest.mark.parametrize(
    "word,expected_error",
    [
        pytest.param([12, 32], TypeError, id="test TypeError"),
    ]
)
def test_raise_error_correctly(word: str, expected_error: Any) -> None:

    with pytest.raises(TypeError):
        is_isogram(word)
