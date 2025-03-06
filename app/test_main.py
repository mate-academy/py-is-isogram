import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "no repeating letters should return True",
        "have repeating letters should return False",
        "have repeating capital letters should return False",
        "empty string should return True"
    ]
)
def test_correct_outcome(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
