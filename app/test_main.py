import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Alphabet", False),
        ("Dermatoglyphics", True),
        ("isogram", True),
        ("noon", False),
        ("Moon", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
