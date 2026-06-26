import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("isogram", True),
        ("moon", False),
        ("backgroun", False),
    ],
)
def test_is_isogram_with_words(word, expected):
    assert main.is_isogram(word) is expected


def test_is_isogram_with_empty_string():
    assert main.is_isogram("") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Mm", False),
        ("ISOGRAM", True),
    ],
)
def test_is_isogram_with_uppercase_letters(word, expected):
    assert main.is_isogram(word) is expected
