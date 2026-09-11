import pytest

from typing import Any

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_word,expected_result",
        [
            (
                "playgrounds", True
            ),
            (
                "look", False
            ),
            (
                "Adam", False
            ),
            (
                "", True
            ),
            (
                "apple", False
            ),
            (
                "cock", False
            )
        ]
    )
    def test_if_is_isogram(self,
                           initial_word: str,
                           expected_result: bool):
        assert is_isogram(initial_word) == expected_result

    @pytest.mark.parametrize(
        "initial_word,expected_error",
        [
            pytest.param(
                7, AttributeError,
                id="error if type has no attribute 'lower'"
            )
        ]
    )
    def test_if_right_error_raising(self,
                                    initial_word: Any,
                                    expected_error: Any):
        with pytest.raises(expected_error):
            is_isogram(initial_word)