import pytest

from app.main import is_isogram


@pytest.mark.parametrize("string, extended", [
    ("mM", False),
    ("Adam", False),
    ("", True),
    (" ", True),
    ("  ", False),
    ("look", False),
    ("lake", True)
])
def test_is_gram(string: str, extended: bool) -> None:
    assert is_isogram(string) == extended
