from typing import Any

import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_value", [
            pytest.param(
                "playgrounds",
                True,
                id="test should return True: all letter in word is different"
            ),
            pytest.param(
                "look",
                False,
                id="test should return False:"
                   "there are several identical letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="test should return False:"
                   "there are several identical letters in different cases"
            ),
            pytest.param(
                "",
                True,
                id="test should return True: empty string"
            )
        ]
    )
    def test_word_is_isogram(
            self,
            word: str,
            expected_value: bool
    ) -> None:

        assert is_isogram(word) == expected_value

    @pytest.mark.parametrize(
        "value", [
            pytest.param(
                ["list"],
                id="test get 'list' should raising AttributeError"
            ),
            pytest.param(
                {"set"},
                id="test get 'set' should raising AttributeError"
            ),
            pytest.param(
                {"dict": 1},
                id="test get 'dict' should raising AttributeError"
            ),
            pytest.param(
                17,
                id="test get 'int' should raising AttributeError"
            )
        ]
    )
    def test_raising_errors_in_is_isogram(
            self,
            value: Any
    ) -> None:

        with pytest.raises(AttributeError):
            is_isogram(value)
