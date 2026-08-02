from app.main import is_isogram
import pytest


class TestIsogram:
    @pytest.mark.parametrize(
        "word,value",
        [
            pytest.param(
                "",
                True,
                id="Test empty string should be True"
            ),
            pytest.param(
                "Adam",
                False,
                id="Test the same letter in different register should be False"
            ),
            pytest.param(
                "look",
                False,
                id="Test consecutive letters should be False"
            )
        ]
    )
    def test_is_isogram(self, word: str, value: bool) -> None:
        assert is_isogram(word) is value
