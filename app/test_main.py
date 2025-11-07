import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        ["word", "expected_result"],
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False)
        ]
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) is expected_result
