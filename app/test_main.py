import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("apple", False),
        ("app", False),
        ("door", False),
        ("abcd", True),
        ("bjk", True),
        ("semen", False),
        ("trash", True),
        ("garbage", False),
        ("boolean", False),
        ("info", True),
        ("", True),
        ("sS", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
