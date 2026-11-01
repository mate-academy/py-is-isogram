import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "",
        "a",
        "playgrounds",
        "abcdefghijklmnopqrstuvwxyz",
    ],
)
def test_is_isogram_returns_true_for_isograms(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "Adam",
        "aba",
        "aabb",
    ],
)
def test_is_isogram_returns_false_for_words_with_repeated_letters(
    word: str,
) -> None:
    assert is_isogram(word) is False


def test_is_isogram_is_case_insensitive() -> None:
    assert is_isogram("Aa") is False
