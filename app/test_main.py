import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_word",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_is_isogram(self, word: str, expected_word: str) -> None:
        assert is_isogram(word) == expected_word
