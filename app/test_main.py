import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return True when all letters are unique"
            ),
            pytest.param(
                "look",
                False,
                id="should return False when letters are repeated"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return False when one letter "
                   "occurs in low and capitalize cases"
            ),
            pytest.param(
                "",
                True,
                id="should return True when string is empty"
            )
        ]

    )
    def test_is_word_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
