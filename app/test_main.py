import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, expected_results",
        [
            pytest.param(
                "playgrounds",
                True,
                id="test isogram"
            ),
            pytest.param(
                "look",
                False,
                id="test not isogram"
            ),
            pytest.param(
                "Adam",
                False,
                id="test case sensitivity"
            ),
            pytest.param(
                "",
                True,
                id="test empty string"
            ),
        ]
    )
    def test_isogram_logical(self,
                             word: str,
                             expected_results: bool) -> None:
        assert is_isogram(word) == expected_results
