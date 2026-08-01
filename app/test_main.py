import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Dermatoglyphics", True),
    ],
    ids=[
        "empty_string",
        "simple_isogram",
        "consecutive_duplicate",
        "case_insensitive_duplicate",
        "long_isogram",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
