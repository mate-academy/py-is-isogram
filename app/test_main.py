from app.main import is_isogram
from typing import Any
import pytest


class TestIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            ("", True),
            ("A", True),
            ("Ww", False),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False)
        ]
    )
    def test_correct_result(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "word",
        [
            (1),
            ([]),
            ({})
        ]
    )
    def test_raises_error_when_wrong_data(self, word: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
