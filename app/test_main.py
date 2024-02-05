from typing import Any, Type

import pytest

from app.main import is_isogram


class TestIsIsogramWords:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            (" playgrounds ", False),
            ("1234567890", True)
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ):
        assert (is_isogram(word) == result)


class TestIsIsogramTypes:
    @pytest.mark.parametrize(
        "word,error",
        [
            (1, AttributeError),
            ([], AttributeError),
            ({}, AttributeError),
            (None, AttributeError)
        ]
    )
    def test_is_isogram_types(
            self,
            word: Any,
            error: Type[Exception]
    ):
        with pytest.raises(error):
            is_isogram(word)
