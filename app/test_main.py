from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            ("", True),
            ("a", True),
            ("ab", True),
            ("aa", False),
            ("A", True),
            ("Aa", False),
            ("aA", False),
            ("aaaa", False),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("1", True),
            ("11", False)
        ],
        ids=[
            "empty string",
            "a letter",
            "two different letters",
            "two same letters",
            "a high register letter",
            "the same letter in high and low register",
            "the same letter in low and high register",
            "string of 4 same letters",
            "string of 4 different letters",
            "word with 2 same letters",
            "word with 2 same letters in high and low register",
            "number",
            "digit with 2 same numbers"
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
