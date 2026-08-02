import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "test_str,expected_bool",
        [
            ("look", False),
            ("Adam", False),
            ("playgrounds", True),
            ("", True),
        ]
    )
    def test_is_isogram(self, test_str: str, expected_bool: bool) -> None:
        assert is_isogram(test_str) == expected_bool
