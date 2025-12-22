import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("abc", True),
        ("Aa", False),
        ("Dermatoglyphics", True),
        ("isogram", True),
        ("moOse", False),
    ],
)
def test_is_isogram(word, expected):
    assert is_isogram(word) is expected
