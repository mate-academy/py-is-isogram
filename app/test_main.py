from app.main import is_isogram
import pytest


class TestStringForBeingIsogram:
    @pytest.mark.parametrize(
        "string_to_check, expected_answer",
        [
            pytest.param(
                "playgrounds",
                True,
                id="all letters are unique, should return True"
            ),
            pytest.param(
                "look",
                False,
                id="1 letter repeats, should return False"
            ),
            pytest.param(
                "Adam",
                False,
                id="upper and lower cases are considered "
                   "to be the same letter, should return False"
            ),
            pytest.param(
                "",
                True,
                id="empty string is an isogram, should return True"
            ),
            pytest.param(
                "aAbBcC",
                False,
                id="no unique letters in string, should return False"
            )
        ]
    )
    def test_letters(
            self,
            string_to_check: str,
            expected_answer: bool
    ) -> None:
        result = is_isogram(string_to_check)
        assert result == expected_answer
