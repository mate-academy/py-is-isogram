import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("ISOGRAM", True),
        ("isoGram", True),
        ("aba", False),
        ("moOse", False),
        ("thumbscrewjapingly", True),
        ("Dermatoglyphics", True),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxyza", False),
    ],
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
