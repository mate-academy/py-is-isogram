import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("aba", False),
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) == expected
