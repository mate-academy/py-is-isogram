import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("word", True),
        ("look", False),
        ("Apple", False),
        ("Banana", False),
        ("", True),
        ("a", True),
        ("aA", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
