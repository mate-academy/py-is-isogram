import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("look", False),
            ("Adam", False),
            ("playgrounds", True),
            ("", True),
        ],
        ids=[
            "word should consist only unique letters",
            "word should consist only unique letters",
            "should return True all letters are unique",
            "should return True if string empty",
        ],
    )
    def test_check_if_word_is_isogram(
            self,
            word: str,
            expected: bool,
    ) -> None:
        assert is_isogram(word) == expected
