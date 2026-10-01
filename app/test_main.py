from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "isogram_input, expected_output",
    [
        (
            "isogram",
            True
        ),

        (
            "",
            True
        ),

        (
            "Pepsi",
            False
        ),

        (
            "Daniil",
            False
        )
    ]
)
def test_is_isogram(isogram_input: str, expected_output: bool) -> None:
    assert is_isogram(isogram_input) is expected_output
