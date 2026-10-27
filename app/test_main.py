import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("Adam", False),
        ("!ok", True),
        ("summer", False),
        ("spring", True),
        ("aba", False),
        ("AbCd", True),
    ]
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) == expected
