import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("isogram", True),
        ("hello", False),
        ("Aba", False),
        ("123", True),
        ("Isogram and me", False),
        ("QwerTyuiopasdFghjklzxcvbnm", True)
    ],
    ids=[
        "Word is empty",
        "Word is isogram in lower case",
        "Word isn`t isogram in lower case",
        "Word isn`t isogram in multy cases",
        "Word is isogram value its a integer",
        "Word isn`t isogram value, it`s a two words",
        "Word is isogram value it`s a big unique string"
    ]
)
def test_main(word: str, result: bool) -> None:
    assert is_isogram(word) == result
