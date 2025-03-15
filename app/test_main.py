from app.main import is_isogram
import pytest


@pytest.mark.parametrize("string, expected", [
    ("mM", False),
    ("Adan", False),
    ("look", False),
    ("  ", False),
    ("", True),
    (" ", True),
    ("Lake", True)
])
def test_is_isogram(string: str, expected: bool) -> None:
    assert is_isogram(string) == expected
