from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize("word,expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("FalsE", True),
        ("tenet", False)
    ])
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
