import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("a", True),
        ("abcdef", True),
        ("aa", False),
        ("abcabc", False),
        ("Aa", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
