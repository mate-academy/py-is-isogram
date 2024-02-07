import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string, expected",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
        ]
    )
    def test_is_isogram(self, string: str, expected: bool) -> None:
        result = is_isogram(string)
        assert result == expected
