import pytest

from .main import is_isogram


def test_notonly_letters_in_arguments() -> None:
    assert (is_isogram("Gkjl2#!@")), "The word should consist of Letters only"


def test_is_isogram_should_return_bool() -> None:
    assert isinstance((is_isogram("World") is False), bool)


def test_capital_letters_same_small_in_arguments() -> None:
    assert (is_isogram("GrilL") is False), \
        "The capital letters same the small"


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "all small letters isogram = True",
        "all small letters not isogram = False",
        "mix letters not isogram = False",
        "the empty string is an isogram",
    ]
)
def test_functionality(word: str,
                       result: bool
                       ) -> None:
    assert (is_isogram(word) == result),\
        (f"Word: {word},should be {result} isogram status")
