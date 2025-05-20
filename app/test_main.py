from app.main import is_isogram
import pytest


class TestIsIsogram:

    @pytest.mark.parametrize("input_word, expected_bool", [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("Adam", False)
    ])
    def test_is_isogram(self, input_word: str, expected_bool: bool) -> None:
        assert is_isogram(input_word) is expected_bool
