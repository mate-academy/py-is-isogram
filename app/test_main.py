import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        (
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ),
        ids=(
            "should return True for long word",
            "should return False for word with duplicates in lowercase",
            "should return False for word with duplicates in different cases",
            "should return True for empty string"
        )
    )
    def test_defines_isogram_correctly(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
