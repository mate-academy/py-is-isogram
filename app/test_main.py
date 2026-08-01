from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("lamp", True),
        ("letter", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
    ],
    ids=[
        "unique_letters",
        "repeated_letters",
        "case_insensitive_false",
        "empty_string",
        "short_isogram",
        "double_letter",
        "mixed_case_true",
        "mixed_case_false",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
