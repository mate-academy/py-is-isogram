from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [("playgrounds", True), ("look", False), ("Adam", False), ("", True)],
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
