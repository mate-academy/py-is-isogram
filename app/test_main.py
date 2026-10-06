import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("ABCdef", True),
        ("look", False),
        ("aa", False),
        ("abca", False),
        ("Adam", False),
        ("aA", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
