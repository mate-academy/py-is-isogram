from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
     ("playgrounds", True),
     ("look", False),
     ("Adam", False),
     ("", True)
    ]
)
def test_is_isogram_valid_input(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
