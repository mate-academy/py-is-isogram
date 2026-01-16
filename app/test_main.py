from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "words,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        " test for long word",
        " test for short word",
        "test for big item",
        "test for nothing",
    ]
)
def test_is_isogram(words: str, result: bool) -> None:
    assert is_isogram(words) == result
