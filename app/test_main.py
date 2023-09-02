from typing import Any
import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param(
                "",
                True,
                id="test is_isogram be empty"
            ),
            pytest.param(
                "apple",
                False,
                id="test is_isogram be repeating letters"
            ),
            pytest.param(
                "machine",
                True,
                id="test is_isogram no repeating letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="test is_isogram be case insensitive"
            )
        ]
    )
    def test_(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "string, exception_err",
        [
            pytest.param(
                {},
                AttributeError,
                id="checks for the input string"
            ),
            pytest.param(
                1,
                AttributeError,
                id="expected error when entering a number"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            string: Any,
            exception_err: Any
    ) -> None:
        with pytest.raises(exception_err):
            is_isogram(string)
