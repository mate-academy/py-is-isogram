import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_word,expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_is_isogram_work_correctly(
            self,
            initial_word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(initial_word) is expected_result, (
            f"Word {initial_word} isn't isogram."
        )
