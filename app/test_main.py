import pytest
from typing import Type


from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("isogram", True),
            ("algorithm", False),
            ("jumbled", False),
            ("subdermatoglyphic", True),
            ("aba", False),
            ("abcabc", False),
            ("abcdefghijklmnopqrstuvwxyz", True),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
            ("1234567890", True),
            ("", True)
        ],
        ids=[
            "simple isogram",
            "simple non isogram",
            "complex non isogram",
            "complex isogram",
            "duplicate letters",
            "duplicate letters with others",
            "all lowercase",
            "all uppercase",
            "digits only",
            "empty string"
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "cents,error",
        [
            pytest.param(1, AttributeError)
        ],
        ids=[
            "not integer type raises exception"
        ]
    )
    def test_is_isogram_error(
            self,
            cents: str,
            error: Type[Exception]
    ) -> None:
        with pytest.raises(error):
            is_isogram(cents)
