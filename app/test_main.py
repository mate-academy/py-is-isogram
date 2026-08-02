import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("look", False),
        ("playgrounds", True),
        ("Adam", False)
    ],
    ids=[
        "check empty string",
        "check same letter of same case",
        "check word with unique letters",
        "check words with same letter but different case"
    ]
)
def test_check_if_word_is_isogam(word: str, result: bool) -> None:
    assert is_isogram(word) == result
