import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,bool_expression",
        [
            ("playgrounds", True),
            ("", True),
            ("Adam", False),
            ("look", False)
        ]
    )
    def test_check_if_is_isogram_returns_correct_bool_value(
            self,
            word: str,
            bool_expression: bool
    ) -> None:

        assert is_isogram(word) == bool_expression
