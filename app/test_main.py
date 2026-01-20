import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "text,expected",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_if_function_return_is_correct(
        self,
        text: str,
        expected: bool
    ) -> None:
        assert is_isogram(text) == expected