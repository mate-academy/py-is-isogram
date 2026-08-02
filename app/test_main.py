from app.main import is_isogram

import pytest

# write your code here


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "Adam", False,
                id="the word: 'Adam' should not be an isogram"
            ),
            pytest.param(
                "DoOde", False,
                id="the word: 'MoOn' should not be not an isogram"
            ),
            pytest.param(
                "", True,
                id="Empty string should be an isogram"

            ),
            pytest.param(
                "QweRt", True,
                id="the word: 'AbCdEfG' should be an isogram"
            )
        ]
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
