from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "actual, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("abcd", True),
        ("Aa", False),
    ],
)
def test_should_return_correctly(actual: str, expected: bool) -> None:
    assert is_isogram(actual) is expected
