import pytest
import app.main


@pytest.mark.parametrize("word, expected", [
    ("", True),  # empty string is an isogram
    ("a", True),  # single letter
    ("playgrounds", True),  # long isogram
    ("subdermal", True),  # another valid isogram
    ("look", False),  # repeated 'o'
    ("hello", False),  # repeated 'l'
    ("Adam", False),  # case-insensitive: 'a' and 'A' are the same
    ("Mama", False),  # case-insensitive repeated letters
    ("Mouse", True),  # mixed case isogram
    ("ABCabc", False),  # all letters repeat case-insensitively
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert app.main.is_isogram(word) is expected
