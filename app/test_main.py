import pytest
from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word_to_test, result",
    [
        pytest.param(
            "playgrounds", True,
            id="Is isogram - only lower cases"
        ),
        pytest.param(
            "GitHub", True,
            id="Is isogram - lower and upper cases"
        ),
        pytest.param(
            "PYTHON", True,
            id="Is isogram - only upper cases"
        ),
        pytest.param(
            "", True,
            id="Is isogram - empty string"
        ),
        pytest.param(
            " ", True,
            id="Is isogram - one space"
        ),
        pytest.param(
            "    ", False,
            id="Is not isogram - multiple spaces"
        ),
        pytest.param(
            "look", False,
            id="Is not isogram - only lower cases"
        ),
        pytest.param(
            "MateAcademy", False,
            id="Is not isogram - lower and upper cases"
        ),
        pytest.param(
            "ADAM", False,
            id="Is not isogram - only upper cases"
        ),
    ]


)
def test_for_valid_input_data(word_to_test: str, result: bool) -> None:
    assert is_isogram(word_to_test) == result


@pytest.mark.parametrize(
    "tested_value, expected_error",
    [
        pytest.param(
            20.15, AttributeError,
            id="input value should not be a float"
        ),
        pytest.param(
            15, AttributeError,
            id="input value should not be a integer"
        ),
        pytest.param(
            ["Visual"], AttributeError,
            id="input value should not be a list"
        ),
        pytest.param(
            (1, 0), AttributeError,
            id="input value should not be a tuple"
        ),
        pytest.param(
            {"one": "word"}, AttributeError,
            id="input value should not be a dict"
        ),
        pytest.param(
            {"case"}, AttributeError,
            id="input value should not be a set"
        )
    ]
)
def test_error_codes(tested_value: Any, expected_error: type) -> None:
    with pytest.raises(expected_error):
        is_isogram(tested_value)
