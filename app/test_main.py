import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param("playgrounds", True, id="simple_isogram"),
        pytest.param("look", False, id="repeating_letters"),
        pytest.param("Adam", False, id="case_insensitive"),
        pytest.param("", True, id="empty_string"),
    ]
)
def test_is_isogram(input_str: str, expected: bool) -> None:
    assert is_isogram(input_str) == expected
