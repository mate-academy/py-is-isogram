from app.main import is_isogram


import pytest


@pytest.mark.parametrize("string, expected", [
    ("", True),
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("abcd", True)
])
def test_is_isogram(string: str, expected: bool) -> None:
    assert is_isogram(string) == expected
