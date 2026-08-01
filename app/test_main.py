from typing import Any
import pytest
from app.main import is_isogram


class TestIsIsogram():
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="all different letters",
            ),
            pytest.param(
                "look",
                False,
                id="there are identical ones"
            ),
            pytest.param(
                "Adam",
                False,
                id="test case insensitive"
            ),
            pytest.param(
                "",
                True,
                id="empty is isogram"
            ),
        ]
    )
    def test_is_isogram_correct(
            self,
            word: str,
            expected: bool) -> None:
        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            pytest.param(
                None,
                AttributeError,
                id="no arguments"
            ),
            pytest.param(
                5,
                AttributeError,
                id="attribute is not str"
            ),
        ]
    )
    def test_is_isogram_error(
            self,
            word: Any,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
