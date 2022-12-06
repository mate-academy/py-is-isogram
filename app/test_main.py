import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_word,expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should check different letter"
            ),

            pytest.param(
                "look",
                False,
                id="should check the same letter"
            ),

            pytest.param(
                "Adam",
                False,
                id="should check uppercase"
            ),

            pytest.param(
                "",
                True,
                id="should check empty str"
            )

        ]
    )
    def test_understatnd_isogram_correctly(
            self,
            initial_word: str,
            expected_result: bool
    ) -> None:
        wrd = initial_word
        assert is_isogram(wrd) == expected_result
