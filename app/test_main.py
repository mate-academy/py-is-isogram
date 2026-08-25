import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Dermatoglyphics", True),
        ("a", True),
        ("aba", False),
        ("moOse", False),
        ("Alphabet", False),
        ("isogram", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
