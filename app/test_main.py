import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,check_is_isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("lOok", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "String with no repeating letters is an isogram",
        "String with repeating letters is not an isogram",
        "String with the same letters in different cases is not an isogram",
        "String with the same letters in different cases is not an isogram",
        "Empty string is an isogram",
    ]
)
def test_is_isogram(word: str, check_is_isogram: bool) -> None:
    assert is_isogram(word) == check_is_isogram
