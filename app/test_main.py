import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result", [
            ("", 1),
            ("a", 1),
            ("aa", 0),
            ("playgrounds", 1),
            ("Adam", 0)
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
