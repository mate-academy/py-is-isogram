import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("abc", True),
        ("look", False),
        ("Adam", False),
    ],
    ids=[
        "Empty string should return True",
        "abc should return True",
        "look should return False",
        "Adam should return False",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
