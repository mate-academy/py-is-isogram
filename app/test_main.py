import pytest

from app.main import is_isogram


class TestIsIsogram():
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("true", True),
            ("false", True),
            ("aboba", False),
            ("38aBoba44", False),
            ("aABb", False),
            ("", True)
        ]
    )
    def test_is_isogram(self, test_input: str, expected: bool) -> None:
        assert is_isogram(test_input) == expected
