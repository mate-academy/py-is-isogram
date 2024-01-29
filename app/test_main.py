import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        ("playgrounds"),
        ("look"),
        ("Adam"),
        ("a"),
        ("")
    ]
)
def test_isogram_with_isogram_word(word: str) -> None:
    assert is_isogram(word)
