import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "inputted_str, expected_result",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True)
     ]
)
def test_if_string_is_isogram(inputted_str: str, expected_result: bool) -> None:
    assert (
        is_isogram(inputted_str) == expected_result
    )
