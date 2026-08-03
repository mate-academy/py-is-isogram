import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("abcdef", True),
        ("banana", False),
    ],
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) is expected
