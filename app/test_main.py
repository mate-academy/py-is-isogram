from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("wGaTT", False),
            ("wgat", True),
            ("", True),
            ("lL", False),
            ("ala", False)

        ],
        ids=[
            "when word is string with upper case letters",
            "when word is string with lower case letters",
            "when word is empty string",
            "when word is with same letter in different case",
            "when word is non-consecutive letters repeat"
        ]
    )
    def test_is_isogram_working_correctly(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
