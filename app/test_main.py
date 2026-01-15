import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("playgrounds", True),
    ("Adam", False),
    ("look", False),
    ("PrOcRRRastInatioN", False),
    ("name", True),
    ("A", True),
    ("PpP", False),
    ("Aa", False),
    ("H2O", True),
    ("TeStInG", False),
    ("Twyndyllyngs", False),
    ("Dermatoglyphics", True),
    ("Python", True),
    ("12345", True),
    ("XyZ123", True),
    ("A1B2C3", True)
])
def test_is_isogram(word: str, expected: bool) -> bool:
    assert is_isogram(word) == expected
