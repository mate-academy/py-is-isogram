from app.main import is_isogram

import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "peanuts",
                True,
                id="Words with no repeating letters are an isogram."
            ),
            pytest.param(
                "",
                True,
                id="Empty string should return `True`."
            ),
            pytest.param(
                "Adam",
                False,
                id="String with different cases of the same letter "
                   "is not an isogram."
            ),
            pytest.param(
                "poor",
                False,
                id="Not only non-consecutive letters are not an isogram."
            )
        ]
    )
    def test_word_checked_correctly(
        self,
        word: str,
        expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
