import pytest
from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_valid_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("subdermatoglyphic") is True  # longest known isogram


def test_should_return_false_for_word_with_repeated_letters() -> None:
    assert is_isogram("look") is False
    assert is_isogram("letter") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False  # A == a
    assert is_isogram("MoOse") is False  # M == m, O == o
    assert is_isogram("Python") is True  # distinct letters


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("aa", False),
        ("aba", False),
        ("abcdef", True),
        ("isogram", True),
        ("Alphabet", False),  # A == a
    ],
)
def test_parametrized_isograms(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
