import pytest
from app.main import is_isogram


class TestBasicCase:
    @pytest.mark.parametrize("word, expected", [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ])
    def test_simple_cases(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
