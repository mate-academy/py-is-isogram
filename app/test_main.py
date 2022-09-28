from app.main import is_isogram
import pytest


class TestIsogramWord:
    @pytest.mark.parametrize("initial_string, expected_result", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ])
    def test_string_for_correct_results(self, initial_string, expected_result):
        assert is_isogram(initial_string) == expected_result
