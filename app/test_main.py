import pytest
from app.main import is_isogram

is_isogram("playgrounds") is True
is_isogram("look") is False
is_isogram("Adam") is False
is_isogram("") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
