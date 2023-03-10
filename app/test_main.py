import pytest

from app.main import is_isogram


class TestIsIsagram:
    @pytest.mark.parametrize(
        "word,result",
        [pytest.param("playgrounds", True, id="should return True"),
         pytest.param("look", False, id="Should return False"),
         pytest.param("Adam", False, id="Should return False"),
         pytest.param("", True, id="should return True")])
    def test_isagram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
