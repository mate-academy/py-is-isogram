from xmlrpc.client import Fault

import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("Adam", False),
        ("a", True)
    ],
    ids=[
        "correct isogram 'playgrounds'",
        "word with repetitive",
        "an empty line is also considered an isogram",
        "Checking for different case letters",
        "A word made up of one letter is an isogram"
    ]
)
def test_(word: str, result: bool) -> None:
    assert (
        is_isogram(word) is result
    ), f"The letters must be unique for the word to be considered an isogram."