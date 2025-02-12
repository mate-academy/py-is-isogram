from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),

        ("background", True),

        ("look", False),
        ("hello", False),

        ("Alphabet", False),
        ("moOse", False),

        ("thumbscrew", True),
        ("eleven", False),

        ("isogram", True),
        ("ISOGRAM", True),
        ("IsOgRaM", True),
    ],
    ids=[
        "empty_string",
        "single_letter",
        "long_isogram",
        "repeated_o",
        "repeated_l",
        "case_insensitive_a",
        "case_insensitive_o",
        "complex_isogram",
        "not_isogram",
        "lowercase_isogram",
        "uppercase_isogram",
        "mixed_case_isogram"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
