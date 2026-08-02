from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "text, expected",
    [
        pytest.param("playgrounds", True, id="should return True"),
        pytest.param("look", False, id="should return False"),
        pytest.param("Adam", False, id="should return False"),
        pytest.param("", True, id="should return True"),
    ]
)
def test_check_param(text: str, expected: str) -> None:
    result = is_isogram(text)
    assert result == expected
