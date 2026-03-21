import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "should return True for string that is isogram",
        "should return False for string that is not isogram",
        "should be case-insensitive",
        "should return True if sting is empty",
    ]
)
def test_is_isogram_function(word: str, result: bool) -> None:
    assert is_isogram(word) is result
