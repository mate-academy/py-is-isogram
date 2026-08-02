from app.main import is_isogram
import pytest


class TestIsIsorgam:
    @pytest.mark.parametrize(
        "input_word,output_result",
        [
            pytest.param(
                "ruslan",
                True,
                id="default input"
            ),
            pytest.param(
                "",
                True,
                id="input str is empty"
            ),
            pytest.param(
                "loop",
                False,
                id="input str is not isogram"
            ),
            pytest.param(
                "SmoOzy",
                False,
                id="string with different registers of latter"
            ),
            pytest.param(
                "Tomato",
                False,
                id="string with not consecutive same letters"
            )
        ]
    )
    def test_is_isogram_with_different_args(self,
                                            input_word: str,
                                            output_result: bool) -> None:

        assert is_isogram(input_word) == output_result
