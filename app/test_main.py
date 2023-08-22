import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playgrounds", True, id="check if count occurrences"
            ),
            pytest.param(
                "look", False, id="check with two occurrences"
            ),
            pytest.param(
                "Adam", False, id="check if upper and lower the same letter"
            ),
            pytest.param(
                "", True, id="check if empty string is isogram"
            )
        ]
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        result = is_isogram(word)

        assert expected_result == result
