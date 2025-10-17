import pytest

from app.main import is_isogram


class TestIsIsogram():
    @pytest.mark.parametrize(
        "string,expected",
        [
            ("aa", False),
            ("Aa", False),
            ("Uniq", True),
            ("1234567", True),
            ("QWERTY", True),
            ("11111", False),
            ("", True),
            ("Hello", False),
            ("look", False),
            ("Adam", False)
        ],
        ids=[
            " aa is not isogram",
            " Aa is not isogram",
            " Uniq is isogram",
            " 1234567 is isogram",
            "QWERTY is isogram",
            "11111 is not isogram",
            "empty field is isogram",
            "Hello is not isogram",
            "look is not isogram",
            "Adam is not isogram"
        ]
    )
    def test_is_isogram(self, string: str, expected: bool) -> None:
        assert is_isogram(string) is expected
