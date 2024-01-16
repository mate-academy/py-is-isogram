from app.main import is_isogram
import pytest


class TestResultIsIsogram:
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
                id="check empty string is isogram"
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
    def test_is_isogram(self, given_word, expected_output):
        assert is_isogram(given_word) == expected_output
