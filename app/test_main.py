import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)
def test_words_double_and_nondouble(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        (13),
        (-2),
        (1.4),
    ],
)
def test_word_types_check(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
