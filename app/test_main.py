import pytest
from typing import Any
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("Babushka", False),
            ("1234567890?", True)
        ]
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) is expected_result

    @pytest.mark.parametrize(
        "wrong_type",
        [
            1,
            None,
            [0, 0],
            {0: 0},
            {0, 0}
        ]
    )
    def test_wrong_type_is_isogram(self, wrong_type: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(wrong_type)
