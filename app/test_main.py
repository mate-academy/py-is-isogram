from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ["playgrounds", True],
        ["look", False],
        ["", True],
        ["Adam", False],
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
