from app.main import is_isogram

import pytest


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word, expected_bool",
        [
            ("", True),
            ("Adam", False),
            ("ZEVS", True),
            ("playgrounds", True),
            ("look", False),
        ],
        ids=[
            "empty must return True",
            "non-consecutive letter count is more than two",
            "true isogram is upper",
            "true isogram is lower",
            "consecutive letter count is more than two",
        ]
    )
    def test_correct_input_is_isogram(
            self,
            word: str,
            expected_bool: bool) -> None:
        assert is_isogram(word) == expected_bool
