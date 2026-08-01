from app.main import is_isogram
import pytest


class TestDifSimpCases:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_different_simple_cases(self, word: str, result: list) -> None:
        assert is_isogram(word) == result
