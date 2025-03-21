from pickle import FALSE

import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string,expected_result",
    [
        pytest.param("", True, id="Empty string should return True"),
        ("playgrounds", True),
        ("Adam", False),
        ("look", False)
    ]
)
def test_is_isogram(input_string, expected_result):
    assert is_isogram(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string,expected_error",
    [
        pytest.param(["str"], AttributeError,
                     id="Should return AttributeError when input is list"),
        pytest.param(54, AttributeError,
                     id="Should return AttributeError when input is integer"),
    ]
)
def test_is_isogram_error(input_string, expected_error):
    with pytest.raises(expected_error):
        is_isogram(input_string)
