import pytest
from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "enter_string,expected_bool",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ],
        ids=[
            "isogram_string",
            "not_isogram_string",
            "not_isogram_string_with_capital",
            "empty_string",
        ]
    )
    def test_pass(self, enter_string: str, expected_bool: bool) -> None:
        assert is_isogram(enter_string) == expected_bool
