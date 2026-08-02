import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("word", True),
        ("hello", False),
        ("darling", True),
        ("concatenation", False),
        ("GOod", False),
        ("soon", False),
        ("", True)
    ]
)
def test_should_return_word_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
