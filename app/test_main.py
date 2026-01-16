from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("AaBbCc", False),  # Not an isogram (case-insensitive)
            ("unique", False),
            ("a", True),  # Single letter is considered an isogram
        ],
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result

    def test_is_isogram_edge_case(self) -> None:
        # Test an edge case with a long word (100 characters)
        long_word = "abcdefghij" * 10
        assert is_isogram(long_word) is False
