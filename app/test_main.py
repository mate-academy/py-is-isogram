import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("abc", True),

        ("playgrounds", True),
        ("look", False),
        ("Adam", False),

        ("Dermatoglyphics", True),
        ("moOse", False),  # o і O

        ("aba", False),
        ("isogram", True),

        ("aaaa", False),

        ("subdermatoglyphic", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
