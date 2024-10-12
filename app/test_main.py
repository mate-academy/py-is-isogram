import pytest

from app.main import is_isogram


class TestIsogramFunk:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="test when should return "
                   "True when there are different letters in the word"
            ),
            pytest.param(
                "look",
                False,
                id="test when should return "
                   "False when there are similar letters in the word"
            ),
            pytest.param(
                "Adam",
                False,
                id="test when should return False "
                   "when there are similar letters upper and lower cases"
            ),
            pytest.param(
                "",
                True,
                id="test when should return True when there is empty string"
            )
        ]
    )
    def test_cases(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
