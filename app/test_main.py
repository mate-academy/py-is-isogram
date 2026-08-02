import pytest
from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="should return 'True'"),
        pytest.param("look", False, id="should return 'False' o = o"),
        pytest.param("Adam", False, id="should return 'False', A = a"),
        pytest.param("", True, id="should return 'True' if word is empty")
    ]
)
def test_should_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word",
    [
        pytest.param([], id="should be type string"),
        pytest.param({}, id="should be type string")
    ]
)
def test_should_raise_type_error(word: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
