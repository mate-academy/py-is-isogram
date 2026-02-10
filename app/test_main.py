from app.main import is_isogram
import pytest


@pytest.mark.parametrize("value, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("Aa", False),
    ("a", True),
    ("", True)
])
def test_should_return_true_if_is_isogram(value: str, expected: str) -> None:
    assert is_isogram(value) == expected
