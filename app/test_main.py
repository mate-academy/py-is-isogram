import pytest


from app.main import is_isogram


class IsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("Aa", False),
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
