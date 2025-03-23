from app.main import is_isogram
import pytest


class TestIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("", True),
            ("playgrounds", True),
            ("integer", False),
            ("parAmEtrize", False),
            ("EXAMPLE", False),
            ("zZ", False),
            ("v", True),
            ("V", True),

        ],
        ids=[
            "Empty word is True",
            "The word is an isogram",
            "The word isn't an isogram",
            "Function is a case-insensitive",
            "Function is a case-insensitive with LOWER case",
            "The words with the repeated letter is False",
            "The words with single letter is True",
            "The words with single letter in Upper case is True",
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
