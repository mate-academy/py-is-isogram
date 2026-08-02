import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, boolean",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("bob", False),
            ("Ok", True)
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            boolean: bool) -> None:
        assert is_isogram(word) == boolean
