from typing import Any

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, result",
    [
        pytest.param("", True, id="The empty string is an isogram!"),
        pytest.param(
            "Adam",
            False,
            id="Function should be case-insensitive "
               "(M and m are considered the same letter)."),
        pytest.param("look", False, id="You have repeating letters!"),
        pytest.param("playgrounds", True, id="Should return 'True'!")
    ]
)
def test_function_is_isogram_right_result(
        string: str,
        result: bool
) -> None:

    assert is_isogram(string) == result


@pytest.mark.parametrize(
    "wrong_argument",
    [
        (123),
        ({2123, 23}),
    ]
)
def test_function_on_right_errors(wrong_argument: Any) -> None:

    with pytest.raises(AttributeError):
        is_isogram(wrong_argument)
        raise TypeError("isogram should be string!")
