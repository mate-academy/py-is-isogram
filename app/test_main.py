import pytest
from app.main import is_isogram


class TestIsIsogramClass:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "",
                True,
                id="Test empty string"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="Test word with no repeating letters"
            ),
            pytest.param(
                "dad",
                False,
                id="Test word with repeating letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="Test word with same big and small letter"
            ),
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
