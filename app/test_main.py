import pytest
from app.main import is_isogram


cases_normal = [
    ("playgrounds", True),
    ("look", False),
    ("programming", False),
]

cases_upper_char = [
    ("Alphabet", False),
    ("Dermatoglyphics", True),
]

cases_unusual = [
    ("", True),
    ("a", True),
    ("bb", False),
]

cases_non_string = [123, 1488, 228]


@pytest.mark.parametrize("word, expected", cases_normal)
def test_cases_normal(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("word, expected", cases_upper_char)
def test_cases_upper_char(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("word, expected", cases_unusual)
def test_cases_unusual(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("word", cases_non_string)
def test_non_string(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
