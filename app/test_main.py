import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_words(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        (15),
        (0),
        (-3)
    ]
)
def test_invalid_types(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
