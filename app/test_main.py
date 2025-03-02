import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("Isogram", True),
    ("Dog", True),
    ("Lamp", True),
    ("Fish", True),
    ("Jump", True),
    ("Apple", False),
    ("Letter", False),
    ("Mississippi", False),
    ("Anna", False),
    ("Adam", False),
    ("", True)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
