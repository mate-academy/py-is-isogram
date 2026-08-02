import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string_, expected",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ],
        ids=[
            "letters must not be repeated",
            "letters must not be repeated",
            "letters must not be repeated",
            "letters must not be repeated",
        ]
    )
    def test_is_isogram(self, string_: str, expected: bool) -> None:
        assert is_isogram(string_) == expected
