from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("cat", True),
        ("letter", False),
        ("a", True),
        ("", True),
        ("Aa", False),
        ("AbC", True),
        ("abca", False),
        ("aA", False),
        ("aa", False),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
)
def test_latter(word: str, result: bool) -> None:
    assert is_isogram(word) is result
