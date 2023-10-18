from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("son", True),
        ("boy", True),
        ("banana", False),
        ("", True),
        ("Adam", False),
        ("look", False),
        ("playgrounds", True)
    ],
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
