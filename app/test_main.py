import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("isogram", True),
        ("hello", False),
        ("world", True),
        ("Python", True),
        ("aba", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
        ("subdermatoglyphic", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
