import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("Home", True),
            ("door", False),
            ("Test", False),
            ("pyTon", True),
            ("", True),
        ]
    )
    def test_is_isogram(self,
                        word: str,
                        expected: bool) -> None:
        assert is_isogram(word) == expected
