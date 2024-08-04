import pytest

from app.main import is_isogram

class TestIsIsogram:
    @pytest.mark.parametrize(
        "word_to_check, is_word_isogram",
        [
            ('playgrounds', True),
            ('look', False),
            ('Adam', False),
            ("", True)
        ]
    )
    def test_is_word_isogram(
            self,
            word_to_check: str,
            is_word_isogram: bool
    ) -> None:
        assert is_isogram(word_to_check) == is_word_isogram
