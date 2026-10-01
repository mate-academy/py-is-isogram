import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("abc", True),
        ("abcA", False),
        ("Bca", True)
    ],
    ids=[
        "empty string",
        "isogram string",
        "isogram true uppercase and lowercase",
        "isogram false uppercase and lowercase"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
