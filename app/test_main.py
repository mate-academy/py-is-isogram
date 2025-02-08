import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,exp_result",
    [
        ["", True],
        ["abcdefghijklmnoprstuvwxyz", True],
        ["Aa", False],
        ["Aba", False],
        ["AbA", False],
        ["a a", False]
    ]
)
def test_is_isogram(word: str, exp_result: bool) -> None:
    assert is_isogram(word) == exp_result
