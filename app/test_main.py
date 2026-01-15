from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "Adam",
                False,
                id="should be case-insensitive"
            ),
            pytest.param(
                "",
                True,
                id="the empty string is an isogram"
            ),
            pytest.param(
                "moose",
                False,
                id="consecutive lower-case not isogram"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) is expected_result
