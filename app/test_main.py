from app.main import is_isogram
import pytest


class TestISIogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_for_checking_is_iogram(self, word, result):
        assert is_isogram(word) == result
