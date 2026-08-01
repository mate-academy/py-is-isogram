import pytest
from app.main import is_isogram

test_data = [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),

    ("Moose", False),
    ("Dermatoglyphics", True),
    ("aba", False),
    ("aA", False),
    ("bBb", False),
    ("Isogram", True),

    ("a", True),
    ("aa", False),
    ("A", True),
]


@pytest.mark.parametrize("word, expected", test_data)
def test_is_isogram_standard_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
