from app.main import is_isogram
import pytest


class TestIsIsogramm:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param("playgrounds", True,
                         id="all lower letter which non-repeating"),
            pytest.param("look", False,
                         id="all lower letter which repeating"),
            pytest.param("Adam", False,
                         id="repeating and upper case letters"),
            pytest.param("", True,
                         id="empty string")
        ]
    )
    def test_is_isogramm(self, word, result):

        assert is_isogram(word) is result
