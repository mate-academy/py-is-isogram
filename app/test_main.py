import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string, expected_bool",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_isogram_correctly(
            self,
            string: str,
            expected_bool: bool
    ) -> None:
        assert is_isogram(string) == expected_bool
