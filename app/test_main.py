import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string, expected_bool",
    [
        pytest.param("", True),
        pytest.param("Adam", False),
        pytest.param("look", False),
        pytest.param("playground", True)
    ]
)
def test_is_isogram(input_string: str, expected_bool: str) -> None:
    assert is_isogram(input_string) == expected_bool
