import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_word, expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_modify_correctly(
            self,
            initial_word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(initial_word) == expected_result
