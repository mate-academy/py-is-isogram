import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Word", True),
        ("HELLO", False),
        ("KEYBOARD", True)
    ],
    ids=[
        "When word in lower case isogram",
        "When word in lower case not isogram",
        "When word title and reapeted letter",
        "Empty string",
        "When title letter isn't repeated",
        "When word in upper case isn't isogram",
        "When word in upper case is isogram"

    ]
)
def test_is_word_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
