import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("uncopyrightable", True),
        ("pneumonoultramicroscopicsilicovolcanoconiosis", False),
        ("I", True),
        ("oo", False),
    ]
)
def test_is_isogram_edge_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
