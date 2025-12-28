from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("python", True),
        ("vikings", False),
        ("GitHub", True),
        ("Mate Academy", False),
        ("student", False),
        ("I", True),
        ("aa", False)
    ]
)
def test_word_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
