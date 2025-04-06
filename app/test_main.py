import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Laser", False),
        ("isogram", True),
        ("isIsogram", False),
        ("Alphabet", False),
    ],
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected