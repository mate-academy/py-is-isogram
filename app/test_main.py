from typing import Type

import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, result",
                         [
                             ("playgrounds", True),
                             ("look", False),
                             ("Adam", False),
                             ("", True),
                             ("DAd", False),
                         ]
                         )
def test_should_return_proper_value(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize("value, expected_exception",
                         [
                             (0, TypeError),
                             ([], TypeError),
                             (123, TypeError),
                             (["b", "c"], TypeError)
                         ]
                         )
def test_should_return_expected_error(
        value: str | int | list,
        expected_exception: Type[Exception],
) -> None:
    with pytest.raises(expected_exception):
        is_isogram(value)
