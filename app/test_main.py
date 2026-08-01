import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        (" ", True),
        ("  ", False),
        ("a", True),
        ("aa", False),
        ("abca", False),
        ("abcd", True),
        ("abcA", False),
        ("55", TypeError),
        ("a5b", TypeError)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    if isinstance(expected, type) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            is_isogram(word)
    else:
        assert is_isogram(word) == expected
