import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            "playground, True",
            "look, False",
            "Adam, False",
            "'', True",
            "Playground, True"
        ],
        ids=[
            "test should return True when word is isogram",
            "test should return False when word is not isogram",
            "String with different cases of the same letter is not an isogram",
            "empty string is isogram"
            "String with different cases of the different letters is an isogram"
        ]
    )
    def test_is_isogram(self,
                        word: str,
                        result: bool
                        ) -> None:
        assert is_isogram(word) == result
