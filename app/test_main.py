import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "", True, id="empty string"
            ),
            pytest.param(
                "Adam", False, id="mixed lower + upper"
            ),
            pytest.param(
                "playgrounds", True, id="no repeating letters"
            ),
            pytest.param(
                "look", False, id="consecutive letters"
            ),
        ],
    )
    def test_is_isodram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
