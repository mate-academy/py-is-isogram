import pytest

from app.main import is_isogram


def test_should_return_bool() -> None:
    assert isinstance(is_isogram("look"), bool), (
        "Function should return a boolean value"
    )


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("look", False),
        ("alphabet", False),
        ("Adam", False),
        ("", True),
        ("a", True),
    ],
    ids=[
        "word without repeating letters is an isogram",
        "capitalized word without repeats is an isogram",
        "consecutive repeating letters are not allowed",
        "non consecutive repeating letters are not allowed",
        "same letter in different cases is a repeat",
        "empty string is an isogram",
        "single letter is an isogram",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected, (
        f"is_isogram('{word}') should return {expected}"
    )
