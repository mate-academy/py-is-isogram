import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("ambidextrously", True)
    ]
)
def test_different_words_for_isogram(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    ), f"{word} should return {expected}"
