import pytest

from app.main import is_isogram


class TestCorrectedResultIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "",
                True,
                id="if 'word' is '' return mast be 'True'"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="letters must not be repeated for a value 'True'"
            ),
            pytest.param(
                "look",
                False,
                id="If letters are repeated the value should be 'False'"
            ),
            pytest.param(
                "Adam",
                False,
                id=("If repeated letters are in different "
                    "case the value should be 'False'")
            )
        ]
    )
    def test_correct_result(
            self,
            word: str,
            result: bool
    ) -> None:

        assert is_isogram(word) == result
