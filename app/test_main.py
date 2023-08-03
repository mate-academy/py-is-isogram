import pytest
from app.main import is_isogram


@pytest.mark.parametrize("value, expected", [
    pytest.param("playgrounds", True, id="value is isogram"),
    pytest.param("look", False, id="value is not isogram"),
    pytest.param("", True, id="empty value"),
    pytest.param("Adam", False, id="value has 1 big and 1 small same letter")
])
def test_is_isogram(value: str, expected: bool) -> None:
    assert is_isogram(value) == expected
