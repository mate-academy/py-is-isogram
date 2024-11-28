import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("helLow", False),
        ("look", False),
        ("tree", False),
        ("", True),
        ("playgrounds", True),
        ("local", False),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
