import pytest

from app.main import is_isogram


def test_empty_arg() -> None:
    assert is_isogram("") is True


@pytest.mark.parametrize(
    "word, expected_bool",
    [
        ("hey", True),
        ("lol", False),
        ("thanks", True),
    ],
)
def test_simple_words_lowercase(word: str, expected_bool: bool) -> None:
    assert is_isogram(word) == expected_bool


@pytest.mark.parametrize(
    "word, expected_bool",
    [
        ("Hamburger", False),
        ("Lol", False),
        ("Berlin", True),
        ("None", False),
    ]
)
def test_simple_words_uppercase(word: str, expected_bool: bool) -> None:
    assert is_isogram(word) == expected_bool


@pytest.mark.parametrize(
    "word, expected_bool",
    [
        ("ExTerNaLRequireMents", False),
        ("QWERTYuiopASDfghq", False),
        ("MENtIo", True),
        ("AAAAAAAAAAA", False),
    ]
)
def test_complex_words(word: str, expected_bool: bool) -> None:
    assert is_isogram(word) == expected_bool
