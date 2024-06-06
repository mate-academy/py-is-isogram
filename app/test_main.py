from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_word,res",
    [
        ["playgrounds", True],
        ["look", False],
        ["", True],
        ["qwertyuio", True],
        ["mM", False],
        ["qwe rtyuio", True],
        ["qwe rty uio", False],
    ]
)
def test_is_isogram(input_word: str, res: bool) -> None:
    assert is_isogram(input_word) == res