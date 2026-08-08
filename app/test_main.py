import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", True),
        ("isogram", True),
        ("look", False),
        ("Dermatoglyphics", True),
        ("Adam", False)
    ]
)
def test_is_isogram(input_string: str, expected_output: bool) -> None:
    assert is_isogram(input_string) == expected_output
