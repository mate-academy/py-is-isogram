from app.main import is_isogram
import pytest


@pytest.mark.parametrize("strings, expected", [
    ("playgrounds", True),
    ("Adam", False),
    ("sjsjdkskkds", False),
    ("qwerty", True),
    ("AAaaAA", False),
    ("", True),
])
def test_of_the_is_isogram(strings: str, expected: bool) -> is_isogram:
    assert is_isogram(strings) == expected
