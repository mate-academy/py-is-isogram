import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize("word,result", [
        pytest.param("", True,
                     id="Empty string should be isogram"),
        pytest.param("JouRneY", True,
                     id="Should be case-insensitive"),
        pytest.param("loOk", False,
                     id="String with different cases of the same letter "
                        "is not an isogram"),
        pytest.param("vacation", False,
                     id="Not only consecutive letters are not an isogram")
    ])
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
