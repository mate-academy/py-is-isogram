import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("subdermatoglyphic", True),
    ("Alphabet", False),
    ("six-year-old", True),
    ("Emily Jung Schwartzkopf", True),
    ("accentor", False),
], ids=[
    "Empty string",
    "Longest known isogram",
    "Case insensitive",
    "With hyphen",
    "With spaces",
    "Non-isogram",
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
