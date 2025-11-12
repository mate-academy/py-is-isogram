import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            ("", True),
            ("a", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False)
        ],
        ids=[
            "empty string",
            "only one letter",
            "standard case with all different letters",
            "two same small letters",
            "case-insensitive test"
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
