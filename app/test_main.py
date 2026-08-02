import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "words, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("a", True),
        ("Moose", False),
        ("Dermatoglyphics", True),
        ("abc", True),
        ("abca", False),
        ("abba", False),
        ("aaa", False),
        ("Aa", False),
    ]
)
def test_is_isogram(words: str, expected: bool) -> None:
    assert is_isogram(words) is expected
