import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_value",
        [
            ("playgrounds", True),
            ("look", False),
            ("Autor", True),
            ("Adam", False),
            ("a", True),
            ("", True),
        ],
        ids=[
            "correct word isogram",
            "word with repeating letter",
            "word with uppercase letter",
            "word with uppercase and repeating",
            "word with one letter",
            "empty string"
        ]
    )
    def test_is_isogram(self, word: str, expected_value: bool) -> None:
        assert (is_isogram(word) is expected_value
                ), "The word must have unique letter for considerate isogram"
