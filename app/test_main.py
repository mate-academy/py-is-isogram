import pytest
from app.main import is_isogram


class TestFunIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param("", True, id="The empty string is an isogram"),
            pytest.param("Adam", False, id="Should be case-insensitive"),
            pytest.param("playgrounds", True, id="This isogram"),
            pytest.param("look", False, id="This not isogram"),
        ]
    )
    def test_parametrize_is_isogram(self, word: str, result: bool) -> None:
        assert (
            is_isogram(word) is result
        )
