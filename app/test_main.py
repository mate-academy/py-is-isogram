from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Isogram", True),
        ("IsoGram", True),
        ("isogram", True),
        ("A", True),
        ("afhijtgu", True),
        ("hjvdfvourr", False),
        ("abcd1234", True),
        ("a-b-c", False),
        ("...", False),
        ("123", True)
    ]
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) == expected
