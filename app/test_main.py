from typing import Type
import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (is_isogram(word), result)


@pytest.mark.parametrize(
    "word, error",
    [
        (0, AttributeError),
        (True, AttributeError),
        (("Look", "Adam"), AttributeError),
        (("Look", "Adam"), AttributeError),


    ]
)
def test_incorrect_input(word: str, error: Type[Exception]) -> None:
    with pytest.raises(error):
        is_isogram(word)
