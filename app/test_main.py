import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "should return True if there are no repeating letters in the word",
        "should return False if there are repeating letters in the word",
        "should return False if repeating letters "
        "in the word are in different register",
        "should return Ttrue if the word is an empty string"
    ]
)
def test_is_isogram_function(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result
