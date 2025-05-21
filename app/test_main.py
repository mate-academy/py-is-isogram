# rer8
import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram,result_bool",
    [
        pytest.param("", True, id="empty_string_then_return_true"),
        pytest.param("isogram", True, id="isogram_then_return_true"),
        pytest.param("look", False, id="look_then_return_false"),
        pytest.param("Adam", False, id="Adam_then_return_false"),
        pytest.param("playgrounds", True, id="playgrounds_then_return_true")
    ])
def test_is_isogram(isogram: str, result_bool: bool) -> None:
    result = is_isogram(isogram)
    assert result == result_bool
