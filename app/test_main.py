from app.main import is_isogram
import pytest


class TestIso:
    @pytest.mark.parametrize(
        "string,expected",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False)
        ]
    )
    def test_cases(self, string: str, expected: bool) -> None:
        assert is_isogram(string) == expected
