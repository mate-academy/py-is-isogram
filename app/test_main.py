from app.main import is_isogram
import pytest
from typing import Any


@pytest.mark.parametrize(
    "word,bool_value",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return true when string correctly"
        ),
        pytest.param(
            "look",
            False,
            id="should return false when more then one letter"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return false when in string"
               " there is an uppercase and a lowercase letter"
        ),
        pytest.param(
            "",
            True,
            id="should return true when the line is empty"
        )
    ]
)
def test_should_return_correct_bool_value(
    word: str,
    bool_value: bool
) -> None:
    assert is_isogram(word) == bool_value


@pytest.mark.parametrize(
    "word,expected_error",
    [
        pytest.param(
            1,
            AttributeError,
            id="should accept str type data"
        )
    ]
)
def test_raising_errors_correctly(
    word: str,
    expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
