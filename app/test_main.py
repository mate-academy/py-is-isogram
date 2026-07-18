import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, bool_result",
        [
            pytest.param(
                "playgrounds", True,
                id="should check no repeating lower letters"
            ),
            pytest.param(
                "PLAYGROUND", True,
                id="should check no repeating upper letters"
            ),
            pytest.param(
                "Playground", True,
                id="should check no repeating lower and upper letters"
            ),
            pytest.param(
                "look", False,
                id="should check consecutive lower repeating letters"
            ),
            pytest.param(
                "Adam", False,
                id="should check non-consecutive upper repeating letters"
            ),
            pytest.param(
                "", True,
                id="should check empty string"
            )
        ]
    )
    def test_isogram(
            self,
            word: str,
            bool_result: bool
    ) -> None:
        assert is_isogram(word) is bool_result
