import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            (
                "",
                True
            ),
            (
                "A",
                True
            ),
            (
                "Aa",
                False
            ),
            (
                "abA",
                False
            ),
            (
                "aba",
                False
            )
        ]
    )
    def test_word(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
