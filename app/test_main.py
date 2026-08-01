import pytest
from app import main


class TestIsIsogramWord:
    @pytest.mark.parametrize(
        "word,bool_statement",
        [
            ("", True),
            ("look", False),
            ("Adam", False),
            ("playgrounds", True),
            ("1234", True),
            ("1231", False),
        ],
        ids=[
            "Empty string",
            "Same letters in string",
            "Same letters different case",
            "Different letters",
            "Different string numbers",
            "Same string number",
        ]
    )
    def test_is_isogram(self, word: str, bool_statement: bool) -> None:
        assert (
            main.is_isogram(word) == bool_statement
        ), f"{word} should be {bool_statement}"
