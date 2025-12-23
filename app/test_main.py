import pytest
from app.main import is_isogram


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "",
                True,
                id="test empty strint"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="test when word is isogram"
            ),
            pytest.param(
                "look",
                False,
                id="test when word is not isogram with consecutive letters"
            ),
            pytest.param(
                "adam",
                False,
                id="test when word is not isogram with non-consecutive letters"
            ),
            pytest.param(
                "Evening",
                False,
                id="test case sensitivity consecutive"
            ),
            pytest.param(
                "AaBbCc",
                False,
                id="test case sensitivity non-consecutive"
            )
        ]
    )
    def test_is_isogram(
        self,
        word: str,
        expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
