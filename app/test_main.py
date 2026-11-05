import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("python", True),
        ("hello", False),
        ("banana", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("aa", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
