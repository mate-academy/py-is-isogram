from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, isogram_bool",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "True Case",
        "False Case",
        "Upper letter",
        "Empty string"
    ]
)
def test_is_isogram(word: str, isogram_bool: bool) -> None:
    assert is_isogram(word) == isogram_bool
