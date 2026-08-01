import pytest

from app.main import is_isogram


class TestWordForIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "",
                True,
                id="empty string should return True"
            ),
            pytest.param(
                "word",
                True,
                id="should return True if every letter is single in `word`"
            ),
            pytest.param(
                "coMmit",
                False,
                id="should return False if `word` has the same letter in "
                   "lower and upper cases"
            ),
            pytest.param(
                "Electricity",
                False,
                id="should return False if `word` has duplicated letters"
            )
        ]
    )
    def test_is_isogram_func(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
