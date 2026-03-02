import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("Car", True),
        ("DEep", False)
    ], ids=[
        "Empty string should be an isogram",
        "Isogram word should return true",
        "Should be case insensitive"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
