from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_str,result",
    [
        ("playgrounds", True),
        ("Mam", False),
        ("", True),
    ]
)
def test_isogram(input_str: str, result: bool) -> None:
    assert is_isogram(input_str) == result
