from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expect",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "word with unique letters",
        "word with duplicate letters",
        "word with uppercase letters",
        "empty word"
    ]
)
def test_should_check_is_isogram(word: str, expect: bool) -> None:
    assert is_isogram(word) == expect
