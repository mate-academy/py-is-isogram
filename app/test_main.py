from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "",
            True,
            id="test should return True when string is empty"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="test should return True when every letter is unique"
        ),
        pytest.param(
            "Adam",
            False,
            id="test should return False "
               "if two same letters are in a different case",
        ),
        pytest.param(
            "look",
            False,
            id="test should return False "
               "when two letters are the same in a word"
        )
    ]
)
def test_check_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
