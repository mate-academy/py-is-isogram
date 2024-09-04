import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word_add,result_isogram",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_repeating_words(
            self,
            word_add: str,
            result_isogram: bool
    ) -> None:
        assert is_isogram(word_add) == result_isogram
