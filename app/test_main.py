from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgronds", True),
        ("", True),
        ("Adam", False),
        ("look", False),
        ("AMBIDESTRO", True),
        ("PLAYGROUNDS", True),
        ("IsograM", True),
        ("ISOGRAM", True),
    ]
)
def test_is_isogram_functionality(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
