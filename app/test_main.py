import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("AbC", True),
            ("a", True)
        ]
    )
    def test_is_isogram(self, test_input: str, expected: bool) -> None:
        assert is_isogram(test_input) == expected
