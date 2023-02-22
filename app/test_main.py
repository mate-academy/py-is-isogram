from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "",
                True,
                id="test return True for empty string"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="test return True for isogram"
            ),
            pytest.param(
                "iSoGraM",
                True,
                id="test return True for isogram with uppercase letters"
            ),
            pytest.param(
                "look",
                False,
                id="test return False for consecutive word"
            ),
            pytest.param(
                "Adam",
                False,
                id="test return False for non isogram"
            )
        ]
    )
    def test_is_isogram(self,
                        word: str,
                        result: bool
                        ) -> None:
        assert is_isogram(word) == result
