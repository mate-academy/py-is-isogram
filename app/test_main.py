import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test(word: str, result: bool):
    assert is_isogram(word) == result
