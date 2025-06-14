from app.main import is_isogram
import pytest
from typing import Any

@pytest.mark.parametrize(
    "word, list_for_bool_value",
    [
        pytest.param(
            "playgrounds",
            True,
            id="all letters are different"
        ),
        pytest.param(
            "look",
            False,
            id="the letter o is repeated"
        ),
        pytest.param(
            "Adam",
            False,
            id="upper and lower case letters are repeated"
        ),
        pytest.param(
            "",
            True,
            id="should return true when the line is empty"
        )
    ]
)
def test_is_isogram(word: str, list_for_bool_value: bool) -> None:
    assert is_isogram(word) == list_for_bool_value


@pytest.mark.parametrize(
    "word, expected_error",
    [
        pytest.param(
            1,
            AttributeError,
            id="should raise error for non-string input"
        )
    ]
)
def test_raising_errors_correctly(word: Any, expected_error: Any) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
