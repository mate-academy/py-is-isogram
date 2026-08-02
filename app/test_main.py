import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param("playgrounds", True,
                         id="should check that word has no repeating letters"),
            pytest.param("look", False,
                         id="should check that word has repeating letters"),
            pytest.param("Adam", False,
                         id=("should check that word has upper "
                             "and lower repeating letters")),
            pytest.param("", True,
                         id="should check empty list")
        ]
    )
    def test_correct_result(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
