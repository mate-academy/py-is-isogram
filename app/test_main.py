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
            "return True for a word that is long",
            "return False for a word containing repeated lowercase letters",
            "return False for a word with duplicates in mixed cases",
            "return True for an empty string"
        )
    )
    def test_defines_isogram_correctly(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
