from typing import Type

import pytest

from app.main import is_isogram


class TestIsIsogramResults:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "playgrounds",
                True
            ),
            pytest.param(
                "look",
                False
            ),
            pytest.param(
                "Adam",
                False
            ),
            pytest.param(
                "",
                True
            )
        ]
    )
    def test_check_isogram_results(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result


class TestExpectedError:
    @pytest.mark.parametrize(
        "word, expected_error",
        [
            pytest.param(
                5,
                AttributeError,
                id="should raise error if values ages is not int"
            )
        ]
    )
    def test_raising_correctly(
            self,
            word: str,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
