import pytest
import app.main as main


DATA = [
    ("", True),
    ("a", True),
    ("playgrounds", True),
    ("Subway", True),
    ("Alphabet", False),
    ("look", False),
    ("Adam", False),
    ("Aa", False),
    ("Noon", False),
    ("12345", True),
    ("11", False),
    ("  ", False),
    ("Specialist", False),
    ("Check", False),
    ("Background", True),
    ("Downstream", True),
    ("Six-year-old", False),
    ("Isogram", True),
]


@pytest.mark.parametrize("word,expected", DATA)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
