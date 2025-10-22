import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Subdermatoglyphic", True),
        ("Mississippi", False),
        ("Alphabet", False),
        ("Dermatoglyphics", True),
    ],
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
