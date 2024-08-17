from app.main import is_isogram
import pytest


class TestIso:
    @pytest.mark.parametrize(
        "string,expected",
        [
            ("", True),
            ("playground", True),
            ("look", False),
            ("adam", False)
        ]
    )
    def test_is_isogram(self, string: str, expected: bool) -> None:
        assert is_isogram(string) == expected
