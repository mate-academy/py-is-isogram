from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_string_isogram(string: str, expected_result: bool) -> None:
    assert is_isogram(string) == expected_result
