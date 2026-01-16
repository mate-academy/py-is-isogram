import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("", True),
        ("A", True),
        ("Adam", False),
        ("adam", False),
        ("look", False),
        ("playgrounds", True),
    ]
)
def test_different_words(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result


def test_should_raise_error_when_word_is_not_string() -> None:
    with pytest.raises(AttributeError):
        is_isogram(3)
