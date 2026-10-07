import pytest
from app.main import is_isogram


class TestWordIsIsogram:
    @pytest.mark.parametrize(
        "word, outcome",
        [
            ("", True),
            ("Adam", False),
            ("Eel", False)
        ]
    )
    def test_word_is_isogram(
        self,
        word: str,
        outcome: bool
    ) -> bool:
        assert is_isogram(word) == outcome
