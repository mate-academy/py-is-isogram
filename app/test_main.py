import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("isogram", True),
            ("eleven", False),
            ("subdermatoglyphic", True),
            ("playgrounds", True),
            ("Look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
