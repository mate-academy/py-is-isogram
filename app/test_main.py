import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("almost", True),
        ("look", False),
        ("playgrounds", True),
        ("Adam", False),
        ("abcd", True),
        ("GHOST", True)
    ]
)
def test_is_isogram(word: str, expected: bool):
    assert is_isogram(word) == expected
