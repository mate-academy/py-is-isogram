import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="word have no letters"),
        pytest.param("playgrounds", True, id="all different letters in word"),
        pytest.param("h", True, id="word with one letter"),
        pytest.param("look", False, id="two same letter"),
        pytest.param("Adam", False, id="same letter in upper and lower case"),
        pytest.param("look", False, id="two same letter"),

    ]
)
def test_correct_function_behavior(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
