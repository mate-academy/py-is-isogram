import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_word_should_no_repeating_letters(
        word: str,
        expected: bool
) -> None:
    assert expected == is_isogram(word)
