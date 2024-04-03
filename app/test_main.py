import pytest

from app.main import is_isogram


class TestCorrectData:
    @pytest.mark.parametrize(
        "string, bool_value",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_correct_data_for_is_isogram_func(
            self,
            string: str,
            bool_value: bool
    ) -> None:
        assert is_isogram(string) == bool_value
