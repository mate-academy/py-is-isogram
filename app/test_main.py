import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param("playgrounds", True, id="check long correct word"),
            pytest.param("look", False, id="check wrong word"),
            pytest.param("Adam", False, id="check case-insensitive"),
            pytest.param("", True, id="check no word"),
        ]
    )
    def test_word_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        result = is_isogram(word)
        assert result == expected
