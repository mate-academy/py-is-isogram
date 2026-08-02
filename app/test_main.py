import pytest
from app.main import is_isogram


def tests_big_small_letters_should_be_the_same() -> None:
    expected = True
    assert is_isogram("Big") == expected


def test_empty_string_should_return_true() -> None:
    expected = True
    assert is_isogram("") == expected


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("rat", True),
    ("Hungry", True),
])
def tests_should_return_true(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("housekeeper", False),
    ("look", False),
    ("Adam", False),
])
def tests_should_return_false(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
