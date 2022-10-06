from app.main import is_isogram
import pytest


class TestRepeatingLetters:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "",
                True,
                id="should return True if string is empty"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return False if letters in different case"
            ),
            pytest.param(
                "look",
                False,
                id="test for word contains repeating letters"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="test for word contains non-repeating letters"
            ),
        ]
    )
    def test_convert_to_1_penny(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
