import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param("playgrounds", True, id="should return True"),
            pytest.param("k", True, id="should return True"),
            pytest.param("J", True, id="should return True"),
            pytest.param("look", False, id="should return False"),
            pytest.param("Adam", False, id="should return False"),
            pytest.param("", True, id="should return True"),
        ],
    )
    def test_if_word_is_isogram_true(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
