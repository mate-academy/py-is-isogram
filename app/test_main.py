import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param("playgrounds", True),
            pytest.param("look", False),
            pytest.param("Adam", False),
            pytest.param("", True),
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
