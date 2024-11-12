import pytest
from typing import Any

from app.main import is_isogram


class TestIsIsogramParametr:

    @pytest.mark.parametrize("word, expected_result", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Mom", False),
        ("asGxwdfgu", False),
        ("", True),
        ("isogram", True),
        ("IsoGram", True),
        ("12345", True),
        ("hello-world", False),
    ])
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert expected_result == is_isogram(word)


class TestIsIsogramErrors:

    @pytest.mark.parametrize("invalid_input", [
        10,
        [10],
        None,
    ])
    def test_is_isogram_type_error(self, invalid_input: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(invalid_input)
