import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        (" ", True),
        ("playgrounds", True),
        ("hello", False),
        ("look", False),
        ("Adam", False),
        ("g", True),
        ("abcABC", False),
        ("Python", True),
        ("", True),
    ],
)
def test_is_isogram(word: str, expected: list) -> None:
    assert is_isogram(word) == expected
