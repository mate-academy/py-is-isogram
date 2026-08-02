from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_data, answer",
    [
        ("", True),
        ("Adam", False),
        ("look", False),
        ("playgrounds", True),
    ]
)
def test_program(input_data: str, answer: bool) -> None:
    assert is_isogram(input_data) is answer
