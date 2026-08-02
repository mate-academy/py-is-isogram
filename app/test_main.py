from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_string, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_isogram_is_detected_correctly(
        input_string: str,
        result: bool
) -> None:
    assert is_isogram(input_string) == result, \
        "Function should determine isogram correctly!"
