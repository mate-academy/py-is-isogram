import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_word_is_isogram(word: str, isogram: bool) -> None:
    assert is_isogram(word) == isogram, \
        f"Method for word: {word} must return {isogram}"


def test_raising_error_correctly() -> None:
    with pytest.raises(AttributeError):
        is_isogram(123)
