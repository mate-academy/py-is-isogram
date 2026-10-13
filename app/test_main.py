import pytest
from app.main import is_isogram


class TestMain:
    @pytest.mark.parametrize(
        "word,expected",
        [
            ("", True),
            ("Vasyl", True),
            ("Kek", False),
            ("Bebrolit", False),
            ("Shpek", True)
        ]
    )
    def test_isogram_is_determined_correctly(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
