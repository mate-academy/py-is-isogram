import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("error", False),
        ("", True),
        ("L", True),
        ("l", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        123,
        15.5,
        None,
        ["test"],
    ]
)
def test_is_isogram_raises_exception_on_invalid_types(word: str) -> None:
    with pytest.raises((TypeError, ValueError)):
        is_isogram(word)
