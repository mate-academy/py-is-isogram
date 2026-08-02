import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("", True),
            ("playgrounds", True),
            ("SOLID", True),
            ("look", False),
            ("Adam", False),
            ("Memory", False),
            ("OOP", False),
        ]
    )
    def test_expected_result(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
