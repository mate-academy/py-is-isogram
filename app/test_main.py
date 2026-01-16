from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="clear word"),
        pytest.param("look", False, id="double 'o'"),
        pytest.param("Adam", False, id="different registers"),
        pytest.param("", True, id="empty quotes"),

    ]
)
def test_works_correctly(word: str, result: bool) -> None:
    assert (is_isogram(word) == result), \
        f"The result of the function for the word {word} must be {result}"
