import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="word is lower and long"),
        pytest.param("look", False, id="with 2 'o' in word"),
        pytest.param("Adam", False, id="in word is 'a' lower and upper"),
        pytest.param("", True, id="word is empty"),
        pytest.param("a", True, id="one letter word")
    ]

)
def test_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word",
    [
        pytest.param(2, id="if word is int"),
        pytest.param(True, id="if word is bool")
    ]
)
def test_errors(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
