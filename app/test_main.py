import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("hello", False),
        ("world", True),
        ("abcdefg", True),
        ("aabbcc", False),
        ("unique", False),
        ("nonisogram", False),
        ("Hello", False),
        ("aA", False),
        ("Aa", False),
        ("aBcDeF", True),
        ("aBcDeFf", False)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
