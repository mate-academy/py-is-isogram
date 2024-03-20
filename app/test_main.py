import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, extended_result",
    [
        ('playgrounds', True),
        ('look', False),
        ('Adam', False),
        ('', True)
    ]
)
def test_word_is_isogram(
        word: str,
        extended_result: bool
) -> None:
    assert is_isogram(word) == extended_result
