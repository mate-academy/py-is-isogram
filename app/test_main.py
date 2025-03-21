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
def test_is_isogram(input_string: str, expected_result: bool) -> None:
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
def test_is_isogram_error(
        input_string: str, expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        is_isogram(input_string)
