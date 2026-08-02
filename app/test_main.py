import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("CrouG", True)
    ]
)
def test_is_word_isogram(word: str, result: bool) -> None:
    assert (is_isogram(word) == result)
