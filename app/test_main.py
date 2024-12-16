import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string_value,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(
        string_value: str,
        expected_result: bool
) -> None:
    assert is_isogram(string_value) == expected_result
