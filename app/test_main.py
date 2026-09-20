import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("apple", False),
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Game", True),
        ("GamePlay", False),
        ("GameOn", True),
        ("a", True),
        ("A", True),
        ("aA", False),
        ("aa", False),
        ("Dermatoglyphics", True)
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert main.is_isogram(word) is expected_result
