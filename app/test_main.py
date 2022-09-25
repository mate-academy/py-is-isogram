from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "", True,
                id="test should return true if the word is an empty line"
            ),
            pytest.param(
                "look", False,
                id="test should return false if the word is not an isogram"
            ),
            pytest.param(
                "Adam", False,
                id="test should return false if the same letters "
                   "have a different registers"
            ),
            pytest.param(
                "playgrounds", True,
                id="test should return true if the word is an isogram"
            )
        ]
    )
    def test_is_isogram(self, word, result):
        assert is_isogram(word) == result
