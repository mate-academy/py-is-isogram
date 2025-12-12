from app.main import is_isogram
import pytest
from typing import Any


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_should_return_correct_statement(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "word",
        [
            None,
            (1, 3),
            ["lool", ],
            {"lool": None},
            4.3
        ]
    )
    def test_should_raise_error(self, word: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
