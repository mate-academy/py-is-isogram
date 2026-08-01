import pytest
import app.main as main


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert main.is_isogram("x") is True
    assert main.is_isogram("X") is True


def test_case_insensitivity() -> None:
    assert main.is_isogram("Aa") is False
    assert main.is_isogram("aA") is False


@pytest.mark.parametrize(
    "word",
    [
        "playgrounds",
        "isogram",
        "Dermatoglyphics",
        "subdermatoglyphic",
    ],
)
def test_true_isograms(word: str) -> None:
    assert main.is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "letter",
        "moOse",
        "bookkeeper",
        "Adam",
    ],
)
def test_false_isograms(word: str) -> None:
    assert main.is_isogram(word) is False


def test_return_type() -> None:
    result = main.is_isogram("any")
    assert isinstance(result, bool)
