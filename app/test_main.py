from app import main
import pytest


class TestIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param("abcd", True, id="abcd"),
            pytest.param("abcda", False, id="abcda"),
            pytest.param("abccdg", False, id="abcd"),
            pytest.param("", True, id="empty"),
            pytest.param("aa", False, id="abcd"),
            pytest.param("aBcD", True, id="diff letters different case"),
            pytest.param("aA", False, id="same letters different case"),
        ], )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert main.is_isogram(word) == expected
