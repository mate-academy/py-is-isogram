import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("Alphabet", False),
        ("a", True),
        ("thumbscrewjapingly", True),
        ("aba", False),
        ("mOose", False),
        ("Dermatoglyphics", True)
    ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) is expected
