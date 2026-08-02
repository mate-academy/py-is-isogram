import pytest
from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("", True),
            ("abcd", True),
            ("aaAAAaaa", False),
            ("Bbbb", False),
            ("Abacd", False),
            ("bABa", False),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("A", True),
            ("AbcD", True)
        ]
    )
    def test_is_word_is_isogram(
            self, word: str, expected: bool
    ) -> None:
        assert is_isogram(word) == expected
