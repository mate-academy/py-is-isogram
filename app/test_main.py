from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,correct",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("adam", False)
    ]
)
def test_all(word: str, correct: bool) -> None:
    assert is_isogram(word) == correct
