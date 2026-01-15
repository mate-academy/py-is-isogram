from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "input_data, answer",
    [
        ("", True),
        ("abc", True),
        ("Aabc", False),
        ("aabc", False),
        ("abac", False)
    ]
)
def test_program(input_data: str, answer: bool) -> None:
    assert is_isogram(input_data) is answer
