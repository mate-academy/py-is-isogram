import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="there are no repeating letters in the word",
        ),
        pytest.param("", True, id="empty string is isogram"),
        pytest.param(
            "look",
            False,
            id="in a word in a word we have a repetition of letters",
        ),
        pytest.param(
            "Adam", False, id="different cases of one letter is a repetition"
        ),
        pytest.param("UP", True, id="word is upper"),
    ],
)
def test_is_isogram_return_correct_true(word: str, result: bool) -> None:
    assert is_isogram(word) == result
