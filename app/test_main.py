from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("lamp", True),
        ("background", True),
        ("hello", False),
        ("isogram", True),
        ("Alphabet", False),
        ("Aaron", False),
        ("moOse", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
