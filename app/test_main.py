import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Dermatoglyphics", True),
        ("isogram", True),
        ("aba", False),
        ("moOse", False),
        ("isIsogram", False),
        ("", True),
        ("Alphabet", False),
        ("Consecutive", False),
        ("Subdermatoglyphic", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
