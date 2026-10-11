import pytest
from app import main


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("Alphabet", False),
        ("aba", False),
        ("moOse", False),
    ],
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert main.is_isogram(word) == expected_result
