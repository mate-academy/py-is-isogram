import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, isogram",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Result is True when the word does not contain "
                   "the same letters"
            ),
            pytest.param(
                "look",
                False,
                id="Result is False when the word contains two identical "
                   "letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="Result is False when the word contains two letter in "
                   "different register"
            ),
            pytest.param(
                "",
                True,
                id="Result is True when the string is empty"
            ),
            pytest.param(
                "regulations",
                True,
                id="Result is True when the long word does not contain "
                   "the same letters"
            )
        ]
    )
    def test_is_isogram(
            self,
            word,
            isogram
    ):
        assert is_isogram(word) == isogram
