import pytest
from app.main import is_isogram


class TestResult:

    @pytest.mark.parametrize(
        "expected_result, actual_result", [
            pytest.param(True, is_isogram(""),
                         id="the empty string is an isogram"),
            pytest.param(False, is_isogram("Mom"),
                         id="function should be case-insensitive"),
            pytest.param(False, is_isogram("look"),
                         id="isogram is a word that hasn't repeating letters")
        ]
    )
    def test_something(self, expected_result, actual_result):
        assert expected_result == actual_result
