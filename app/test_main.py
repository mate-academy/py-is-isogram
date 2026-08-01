import pytest
from typing import Any

from app.main import is_isogram


@pytest.mark.parametrize(
    "initial_value, expected_bool",
    [
        pytest.param(
            "playgrounds",
            True,
            id="word without repeating letters"
        ),
        pytest.param(
            "look",
            False,
            id="word with consecutive repeating letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="case-insensitive duplicate (A and a)"
        ),
        pytest.param(
            "55555",
            False,
            id="non-letter value as string"
        ),
        pytest.param(
            "OOOOO",
            False,
            id="word with all repeating letters"
        ),
        pytest.param(
            "",
            True,
            id="empty string is isogram"
        ),
    ]
)
def test_function_works_correctly(
        initial_value: str,
        expected_bool: bool
) -> None:
    assert is_isogram(initial_value) is expected_bool


@pytest.mark.parametrize(
    "invalid_value",
    [
        pytest.param(
            36,
            id="integer input"
        ),
        pytest.param(
            None,
            id="None input"
        ),
        pytest.param(
            [10],
            id="list input"
        ),
        pytest.param(
            {"value": 10},
            id="dict input"
        )
    ]
)
def test_raises_type_error_for_invalid_input(invalid_value: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(invalid_value)
