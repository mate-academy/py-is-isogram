import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram(test_input: str, expected: str) -> None:
    assert is_isogram(test_input) == expected
