import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("Adam", False),
        ("look", False),
        ("playgrounds", True)
    ],
    ids=[
        "In this task the '' empty string is an isogram",
        "Must return False because 'Adam' is not an isogram",
        "Must return False because 'look' is not an isogram",
        "Must return True because 'playgrounds' is an isogram"
    ]
)
def test_check_is_word_isogram(
        word: str,
        result: bool) -> None:
    assert is_isogram(word) == result
