import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Isogram", True),
        ("Alphabet", False),
        ("background", True),
        ("six-year-old", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
    ],
    ids=[
        "normal isogram",
        "repeating letter",
        "case insensitive repeat",
        "empty string",
        "isogram with mixed case",
        "non-isogram with case repeat",
        "another normal isogram",
        "non-letter characterpytest app/s (ignored case)",
        "long real isogram",
        "repeat because of case",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
