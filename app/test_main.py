import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("Alphabet", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
        ("subdermatoglyphic", True),
    ],
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_case_insensitivity() -> None:
    assert is_isogram("Aa") is False
    assert is_isogram("BbCcDd") is False
    assert is_isogram("Qwerty") is True


def test_is_isogram_invalid_input() -> None:
    with pytest.raises((TypeError, ValueError)):
        is_isogram(123)
