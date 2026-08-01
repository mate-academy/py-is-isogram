from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("", True),
            ("abc", True),
            ("aabc", False),
            ("Aabc", False),
            ("abcabc", False),
            ("abcDEFR", True),
        ],
        ids=[
            "empty string",
            "no repeats",
            "single repeat",
            "case insensitive repeat",
            "multiple repeats",
            "case insensitive no repeats"
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
