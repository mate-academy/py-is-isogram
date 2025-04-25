import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word", "expected_word",
    [
        is_isogram('playgrounds') is True
        is_isogram('look') is False
        is_isogram('Adam') is False
        is_isogram('') is True
    ]
)
def test_is_isogram(word: str, expected_word: str) -> None:
    assert is_isogram(word) == expected_word
