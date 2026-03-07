import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("subdermatoglyphic", True),
    ("a", True),
    ("", True),
    ("look", False),
    ("Adam", False),
    ("hello", False),
    ("Mama", False),
    ("isIsogram", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("ADAM") is False


def test_raises_type_error_for_non_string_input() -> None:
    with pytest.raises((TypeError, AttributeError)):
        is_isogram(123)
