import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="result is True when no duplicated letters in the word"
            ),
            pytest.param(
                "programming",
                False,
                id="result is False when duplicated letters in the word"
            ),
            pytest.param(
                "abcABC",
                False,
                id="in function uppercase letter value is same as lowercase"
            ),
            pytest.param(
                "",
                True,
                id="Empty string is an isogram"
            ),

        ]
    )
    def test_function_check_words_correctly(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
