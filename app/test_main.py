import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string, expected",
        [
            ("playground", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ],
        ids=[
            "playground_is_isogram",
            "look_is_not_isogram",
            "Adam_is_not_isogram",
            "empty_string_is_isogram"
        ]
    )
    def test_is_isogram(self, string: str, expected: bool) -> None:
        assert is_isogram(string) == expected
