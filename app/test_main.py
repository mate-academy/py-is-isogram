from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "string, expected_result",
    [
        pytest.param("playgrounds ", True, id="should return true"),
        pytest.param("12345", True, id="should return true"),
        pytest.param("1_2_3_4_5", False, id="should return false"),
        pytest.param("look", False, id="should return false"),
        pytest.param("Adam", False, id="should return false"),
        pytest.param("", True, id="should return true"),
        pytest.param("Long!!", False, id="should return false"),
        pytest.param("HELLO!", False, id="should return false")
    ]
)
def test_should_return_correct_result(
        string: str,
        expected_result: bool
) -> None:
    assert is_isogram(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_error",
    [
        pytest.param(3,
                     AttributeError,
                     id="should raise error if string parameter is int type"),
    ]
)
def test_for_raising_error_correctly(
        string: str,
        expected_error: bool
) -> None:
    with pytest.raises(expected_error):
        is_isogram(string)
