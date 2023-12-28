from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result", [
            pytest.param(
                "",
                True,
                id="should return true when string is empty"
            ),
            pytest.param(
                "ASdfGHjkL:",
                True,
                id="should work properly with any case"
            ),
            pytest.param(
                "playgrounds:",
                True,
                id="should return true for word playgrounds"
            ),
            pytest.param(
                "look:",
                False,
                id="should return false for word look"
            ),
            pytest.param(
                "Adam:",
                False,
                id="should return false for word Adam"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert (
            is_isogram(word) == result
        )
