import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
    ]
)
def test_empty_string_returns_true(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("planet", True),
        ("script", True),
    ]
)
def test_word_with_unique_letters_returns_true(word: str,
                                               expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("look", False),
        ("Adam", False),
        ("Less", False),
    ]
)
def test_word_with_repeated_letters_returns_false(word: str,
                                                  expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Adam", False),
        ("Letter", False),
        ("coffee", False),
        ("LamP", True),
        ("Brick", True),
        ("Keyboard", True),
    ]
)
def test_case_insensitive_behavior(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("subdermatoglyphic", True),
        ("uncopyrightable", True),
        ("dermatoglyphics", True),
    ]
)
def test_long_unique_word_returns_true(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected
