from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "input_word,res",
    [
        ["playgrounds", True],
        ["look", False],
        ["Adam", False],
        ["", True],
    ]
)
def test_isogram(input_word: str, res: bool) -> None:
    assert is_isogram(input_word) == res
