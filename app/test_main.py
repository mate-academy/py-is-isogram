import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected", [
        ("playgrounds", True),
        ("look", False),
        ("Arda", False),
        ("", True),
        ("abc", True),
        ("aA", False),
        ("letter", False),
        ("abcdefg", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
