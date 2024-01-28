import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("look", False),
        ("Man", True),
        ("Adam", False),
    ]
)
def test_word_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
