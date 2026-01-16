import pytest
from typing import Any

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("playground", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("Moomin", False),
            ("moomin", False),
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "word",
        [
            None,
            123,
            [],
            {},
            set(),
            tuple(),
            12.3,
            True,
        ]
    )
    def test_is_isogram_invalid_input(self, word: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
