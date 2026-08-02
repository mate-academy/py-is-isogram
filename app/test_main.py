import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,is_isogram_word",
        [
            pytest.param(
                "",
                True,
                id="must return True for empty string"
            ),
            pytest.param(
                "a",
                True,
                id="must return True if len(word) == 1"
            ),
            pytest.param(
                "Playgrounds",
                True,
                id="must return True for isogram word"
            ),
            pytest.param(
                "Tall",
                False,
                id="must return False if there's two or more same letters"
            ),
            pytest.param(
                "suSpect",
                False,
                id="must return False if there two letters in different cases"
            )
        ]
    )
    def test_is_isogram(self,
                        word: str,
                        is_isogram_word: bool) -> None:
        assert is_isogram(word) == is_isogram_word
