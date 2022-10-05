from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "words, output",
    [
        ("", True),
        ("playgrounds", True),
        ("Yes", True),
        ("o", True),
        ("Look", False),
        ("Vacation", False),
        ("Yesterday", False),
        ("Adam", False),
    ]
)
def test_is_isogram(words: str, output: bool) -> None:
    assert is_isogram(words) == output
