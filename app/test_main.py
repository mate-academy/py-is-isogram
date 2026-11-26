import pytest

from app import main


@pytest.mark.parametrize(
    "word",
    [
        "",
        "a",
        "playgrounds",
        "python",
        "lamp",
        "WORLD",
        "Dermatoglyphics",
    ],
)
def test_should_return_true_for_isograms(word: str) -> None:
    assert main.is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "letter",
        "hello",
        "banana",
        "Adam",
        "Aa",
        "aA",
        "Alphabet",
    ],
)
def test_should_return_false_for_non_isograms(word: str) -> None:
    assert main.is_isogram(word) is False
