import app.main as main
import pytest


@pytest.mark.parametrize(
    "word, result",
    [  
        ("mama", False),
        ("Mama", False),
        ("loiut", True),
        ("Loliu", False),
        ("", True),
        ("playgrounds", True),
    ]
)
def test_is_isogram_examples(word: str, result: bool) -> None:
    out = main.is_isogram(word)
    assert isinstance(out, bool), "Return type must be boolean"
    assert out == result, f"Output {out} should be {result}"


@pytest.mark.parametrize("word", [
    "aa",
    "book",
    "letter",
    "BooK",
    "committee",
])
def test_consecutive_letters_are_not_isogram(word):
    assert main.is_isogram(word) is False
