import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False)

        ],
        ids=[
            "Empty string should return True",
            "An isogram word should return True",
            "Repetition of two small letters should return False",
            "Double lower/apper letters should return False"
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
