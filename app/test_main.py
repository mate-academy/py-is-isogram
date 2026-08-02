import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize("word, expected_result", [
        pytest.param("", True,
                     id="should return True if word is ''"),
        pytest.param("playgrounds", True,
                     id="should return True if word have not 2 same latter"),
        pytest.param("look", False,
                     id="should return False if word have 'oo'"),
        pytest.param("Adam", False,
                     id="should return False if word have 'A' and 'a'")
    ])
    def test_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
