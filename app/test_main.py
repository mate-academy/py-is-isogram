import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("asdfghjkl;", True),
        ("doomk", False),
        ("Buibnm", False),
        ("", True),
        ("yui", True),
        ("Bb", False),
        ("Dasfglui", True),
        ("vbnmcxz", True),
        ("gkJjbn", False),
    ],
)

def test_is_isogram(word: str, expected: bool):
    assert is_isogram(word) == expected