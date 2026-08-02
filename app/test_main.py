import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,bool_out",
        [
            pytest.param(
                "",
                True,
                id="The empty string is an isogram."
            ),
            pytest.param(
                "AaBbCc",
                False,
                id="Function should be case-insensitive."
            ),
            pytest.param(
                "XyZiJk",
                True,
                id="There are unique letters. Should return True"
            ),
            pytest.param(
                "AaBbCcXyZiJk",
                False,
                id="There are unique and repetitive letters. "
                   "Should return False"
            )
        ]
    )
    def test_check_output_is_isogmam(self, word: str, bool_out: bool) -> None:
        assert id(is_isogram(word)) == id(bool_out)
