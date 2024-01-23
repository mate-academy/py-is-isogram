from app.main import is_isogram
import pytest


class TestIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param("", True),
            pytest.param("a", True),
            pytest.param("A", True),
            pytest.param("aA", False),
            pytest.param("playgrounds", True),
            pytest.param("look", False),
            pytest.param("Adam", False),
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) is result
