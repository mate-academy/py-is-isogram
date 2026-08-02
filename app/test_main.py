import pytest
from app.main import is_isogram


class TestClass:

    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_that_cower_all(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
