from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word , expected",
    [
        ("playgrounds", True),
        ("adam", False),
        ("PlAyGrOuNds", False),
        ("", True),
        ("gagarin", False),
        ("GaGarIn", False),
        ("look", False)
    ]
)
def test_word_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
