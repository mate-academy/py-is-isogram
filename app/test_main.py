from typing import Any
import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "", True
        ),
        pytest.param(
            "123", True
        ),
        pytest.param(
            "play", True
        ),
        pytest.param(
            "21341", False
        ),
        pytest.param(
            "Test", False
        ),
        pytest.param(
            "test", False
        ),

    ]
)
def test_is_isogram_return_correct_bool(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word, error",
    [
        pytest.param(
            ["word"], AttributeError
        ),
        pytest.param(
            1, AttributeError
        ),
    ]
)
def test_is_isogram_raise_correct_error(word: Any, error: Exception) -> None:
    with pytest.raises(error):
        is_isogram(word)
