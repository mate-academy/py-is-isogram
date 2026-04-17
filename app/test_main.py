import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),

        ("a", True),
        ("A", True),

        ("playgrounds", True),
        ("BACKGROUND", True),
        ("Machine", True),

        ("look", False),
        ("aba", False),
        ("BOOKKEEPER", False),

        ("Adam", False),
        ("Aa", False),
        ("aA", False),
        ("mOose", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
