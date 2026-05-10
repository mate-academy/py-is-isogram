import pytest
from typing import Any
from app import main

class TestIsIsogramFunction:
    @pytest.mark.parametrize(
        "word, bool_value",
        [
            pytest.param(
                "",
                True,
                id="test_empty_string"
            ),
            pytest.param(
                "pLayGrounDs",
                True,
                id="test_different_regist_in_word_isogram"
            ),
            pytest.param(
                "orange",
                True,
                id="test_word_lowercase_is_isogram"
            ),
            pytest.param(
                "GOD",
                True,
                id="test_word_is_isogram_upper_case"
            ),
            pytest.param(
                "Adam",
                False,
                id="test_word_is_not_isogram_lowercase"
            ),
            pytest.param(
                "APPLE",
                False,
                id="test_word_uppercase_is_not_isogram"
            ),
            pytest.param(
                "BoOk",
                False,
                id="test_word_is_not_isogram_different_case"
            )
        ]
    )
    def test_is_isogram_correctly(self, word: str, bool_value: bool)  -> None:
        assert main.is_isogram(word) == bool_value

    @pytest.mark.parametrize(
        "invalid_input",
        [
            124,
            ["s", "t", "r"],
            None
        ]
    )
    def test_is_isogram_invalid_types(self, invalid_input: Any) -> None:
        with pytest.raises(Exception):
            main.is_isogram(invalid_input)