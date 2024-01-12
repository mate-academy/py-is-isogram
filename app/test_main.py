from app.main import is_isogram
import pytest


class TestResultsIsIsogram:
    @pytest.mark.parametrize(
        "given_word,expected_output",
        [
            pytest.param(
                "pool",
                False,
                id="check lowercase not isogram"
            ),
            pytest.param(
                "",
                True,
                id="check empy string is isogram"
            ),
            pytest.param(
                "Carmen",
                True,
                id="check isogram on the right answer"
            ),
            pytest.param(
                "Squids",
                False,
                id="check case-insensitive not isogram"
            ),
        ],
    )
    def test_isogram_on_correct_answer(self, given_word: str, expected_output: bool) -> None:
        assert is_isogram(given_word) == expected_output
