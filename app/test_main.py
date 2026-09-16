import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("isogram", True),
        ("Isogram", True),
        ("hello", False),
        ("world", True),
        ("Python", True),
        ("Pythonista", False),
        ("Pythonista", False),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
