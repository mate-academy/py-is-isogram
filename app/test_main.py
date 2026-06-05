import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("PlayGrounds", True),
        ("Adam", False),
    ],
    ids=[
        "should return True if the string is empty",
        "should return True if the letters are not repeat",
        "should return False if the letters are repeat",
        "should return True if the big letters are not repeat",
        "should return False if the big letters are repeat"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
