import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "Works with no repeating letters in word",
        "Works with repeating letters in word",
        "Function is case-insensitive",
        "Empty string is isogram"
    ]
)
def test_isogram_should_analise_words(word: str, result: bool) -> None:
    assert is_isogram(word) == result
