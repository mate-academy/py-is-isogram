from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "initial_string,expected_output",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_empty_string_should_be_isogram(
        initial_string: str,
        expected_output: bool
) -> None:
    assert is_isogram(initial_string) == expected_output
