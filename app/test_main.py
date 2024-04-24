import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("look", False),
        ("Adam", False),
        ("COveR", True),
        ("", True),
    ],
    ids=[
        "If letter in word repeat, return False",
        "The value is not case sensitive",
        "The value is not case sensitive",
        "If string is empty, return True"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
