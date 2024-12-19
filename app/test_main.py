import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word, result",
    [
        ("", True),
        ("Python", True),
        ("isogram", True),
        ("BlAze", True),
        ("MANGO", True),
        ("flUTE", True),
        ("Letter", False),
        ("balloon", False),
        ("MiSsisSippI", False),
        ("SuCcess", False),
        ("COMMITTEE", False)
    ]
)
def test_is_isogram_generally(
        input_word: str,
        result: bool
) -> None:
    assert is_isogram(input_word) == result


def test_if_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Python") is True
    assert is_isogram("python") is True
    assert is_isogram("pytHOn") is True


def test_should_not_have_repeating_non_consecutive_letters() -> None:
    assert is_isogram("machine") is True
    assert is_isogram("character") is False
    assert is_isogram("elephant") is False


def test_should_not_have_repeating_consecutive_letters() -> None:
    assert is_isogram("balloon") is False
    assert is_isogram("committee") is False


def test_should_not_have_repeating_letters_in_different_cases() -> None:
    assert is_isogram("Elephant") is False
    assert is_isogram("balloOn") is False
