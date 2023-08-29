import pytest
from typing import Any
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "string, result",
        [
            ("Adam", False),
            ("", True),
            ("Mate", True),
            ("playgrounds", True),
            ("process", False)
        ]
    )
    def test_is_isogram(self, string: str, result: bool) -> None:
        assert is_isogram(string) == result

    @pytest.mark.parametrize(
        "string, expected_error",
        [
            ({}, AttributeError),
            (1, AttributeError),
        ]
    )
    def test_raising_error_correctly(
            self,
            string: Any,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(string)
