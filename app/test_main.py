import pytest
from typing import Any

from app.main import is_isogram


class TestCheckEdgeCases:
    @pytest.mark.parametrize(
        ("str_input", "expected_result"),
        [
            pytest.param(
                "", True,
                id="test should return True when input is empty string"
            ),
            pytest.param(
                "playgrounds", True,
                id="test should return true in normal case"
            ),
            pytest.param(
                "look", False,
                id="test should return false with consecutive letters"
            ),
            pytest.param(
                "Adam", False,
                id="""test should return false with non-consecutive letters
                and be case insensitive"""
            ),
        ]
    )
    def test_checking_edge_cases(self,
                                 str_input: Any,
                                 expected_result: Any
                                 ) -> None:
        assert is_isogram(str_input) == expected_result
