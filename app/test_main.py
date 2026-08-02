import pytest

from app.main import is_isogram


class TestIsogrem:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("word", True),
            ("Adam", False),
            ("Mam", False),
            ("background", True),
            ("moOse", False),
            ("", True),
        ]
    )
    def test_words_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
