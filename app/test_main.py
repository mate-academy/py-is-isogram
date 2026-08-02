import pytest
from app.main import is_isogram


class TestIsIsogram():
    @pytest.mark.parametrize(
        "word, boolean_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="no one letter consecutive"
            ),
            pytest.param(
                "look",
                False,
                id="letters in lowercase are repeating"
            ),
            pytest.param(
                "Adam",
                False,
                id="letters in mixed case are repeating"
            ),
            pytest.param(
                "TEST",
                False,
                id="letters in uppercase are repeating"
            ),
            pytest.param(
                "",
                True,
                id="check empty string"
            )
        ]
    )
    def test_modify_correctly(self, word: str, boolean_result: bool) -> None:
        assert is_isogram(word) == boolean_result
