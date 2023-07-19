from app.main import is_isogram
from typing import Type
import pytest


@pytest.mark.parametrize(
    "word,expected_result",
    [("playground", True),
     ("", True),
     ("look", False),
     ("Adam", False),
     ("develop", False),
     ("documentary", True),
     ("Filmography", True)]
)
def test_if_return_is_correct(
        word: str,
        expected_result: bool) -> None:
    assert expected_result == is_isogram(word)


@pytest.mark.parametrize(
    "word,expected_error",
    [(2, AttributeError),
     ({"look"}, AttributeError),
     ((14, 23), AttributeError),
     (["15, 15"], AttributeError)]
)
def test_raise_errors_correctly(
        word: str,
        expected_error: Type[BaseException]) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
