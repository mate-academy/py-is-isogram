from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "words, bool_result",
        [
            pytest.param(
                "playGrounds",
                True,
                id="When word that has no repeating letters, "
                   "return True"
            ),
            pytest.param(
                "look",
                False,
                id="When word that has repeating letters, "
                   "return False"
            ),
            pytest.param(
                "",
                True,
                id="The empty string is an isogram, "
                   "return True"
            ),
            pytest.param(
                "Adam",
                False,
                id="When word that has repeating letters,"
                   "function should be same case,"
                   "return False"
            )
        ]
    )
    def test_isogram(self,
                     words: str,
                     bool_result: bool) -> None:
        assert is_isogram(words) == bool_result
