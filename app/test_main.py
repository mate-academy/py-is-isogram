from app.main import is_isogram
import pytest


class TestIsIsogram:

    @pytest.mark.parametrize("word,expected", [
        pytest.param("bird", True, id="bird"),
        pytest.param("solo", False, id="consecutive"),
        pytest.param("moon", False, id="non-consecutive"),
        pytest.param("SOlo", False, id="different cases word"),
        pytest.param("", True, id="empty string"),
    ])
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
