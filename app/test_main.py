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
def test_is_isogram_returns_correct_boolean_value(
        test_input: str,
        expected: bool
) -> None:
    assert is_isogram(test_input) == expected, (
        f"Expected '{test_input}' should be "
        f"'{not expected}' but got '{expected}'"
    )
