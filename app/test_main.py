import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "given_input, expected_output",
    [
        pytest.param("", True),
        pytest.param("Adam", False),
        pytest.param("look", False),
        pytest.param("playground", True)
    ]
)
def test_is_isogram(given_input: str, expected_output: str) -> None:
    assert is_isogram(given_input) == expected_output
