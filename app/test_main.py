import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_expected_values_are_correct(
        self,
        word: str,
        result: bool
    ) -> None:
        assert is_isogram(word) == result
