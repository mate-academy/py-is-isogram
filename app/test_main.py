import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("isogram", True),
        ("isogramm", False),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "isogram",
        "not_isogram",
        "not_isogram_look",
        "not_isogram_Adam",
        "empty_string",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
