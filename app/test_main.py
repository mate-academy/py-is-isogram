import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "Should return True if word is isogram",
        "Should return False if word isn't isogram",
        "Should return False if word capitalise and isn't isogram",
        "Should return True if word is empty string"
    ]
)
def test_should_return_correct_value(word: str, result: bool) -> None:
    assert is_isogram(word) == result
