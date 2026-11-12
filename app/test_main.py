import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "",
        "a",
        "playgrounds",
        "Python",
        "abcdefghijklmnopqrstuvwxyz",
    ],
)
def test_should_return_true_when_word_is_isogram(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "abca",
        "Adam",
        "aA",
        "abcda",
        "abcdefghijklmnopqrstuvwxyza",
    ],
)
def test_should_return_false_when_word_is_not_isogram(word: str) -> None:
    assert is_isogram(word) is False
