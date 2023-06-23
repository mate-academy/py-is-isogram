from app.main import is_isogram

import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,b_ool",
        [
            pytest.param(
                "",
                True,
                id="should return true for empty string"
            ),
            pytest.param(
                "Mamont",
                False,
                id="String with different cases of same later return False"
            ),
            pytest.param(
                "mmont",
                False,
                id="String with consecutive same later return False"
            )
        ]
    )
    def test_correct_return(
            self,
            word: str,
            b_ool: bool
    ) -> None:
        assert is_isogram(word) == b_ool
