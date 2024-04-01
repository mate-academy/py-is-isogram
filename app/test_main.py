import pytest
from app.main import is_isogram


class TestCoinCombination:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_get_coin_combination(self,
                                  word: str,
                                  expected_result: bool) -> None:
        assert is_isogram(word) is expected_result
