from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize("word, expected", [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("aDAm", False),
        ("hello123", False),
        ("hello!@#$", False),
        ("alphabet", False),
        ("a", True),
        ("alphabet zoo", False),
    ])
    def test_is_isogram(self, word: str, expected: str) -> None:
        assert is_isogram(word) == expected
