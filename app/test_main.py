import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_word,expected_bool_result",
        [
            pytest.param("", True,
                         id="Empty string should be an isogram"),
            pytest.param("Adam", False,
                         id="Should be case insensitive"),
            pytest.param("playgrounds", True,
                         id="Should return true when chr no occur in a word"),
            pytest.param("a", True,
                         id="Should return True when one letter only"),
            pytest.param("Ababahalamaha", False,
                         id="Should return false when more than 2 occur"),
            pytest.param("toolh", False,
                         id="Should return false with consecutive letters"),
            pytest.param("toboth", False,
                         id="Should return false with no-consecutive letters"),
            pytest.param("abcdefghijklmnopqrstuvwxyz", True,
                         id="Should return true with consecutive letters"),
            pytest.param("asdfghdtr", False,
                         id="Should return true with consecutive letters")
        ]
    )
    def test_is_isogram(self,
                        input_word: str,
                        expected_bool_result: bool) -> None:
        assert is_isogram(input_word) == expected_bool_result
