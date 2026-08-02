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
        ("moOse", False),
        ("aba", False),
        ("", True),
        ("isIsogram", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> bool:
    assert is_isogram(word) == expected
