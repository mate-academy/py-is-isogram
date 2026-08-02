import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param(
                "Dermatoglyphics", True,
                id="isogram with unique characters"
            ),
            pytest.param(
                "isogram", True,
                id="isogram with repeated characters"
            ),
            pytest.param(
                "moose", False,
                id="not isogram with repeated characters"
            ),
            pytest.param(
                "", True,
                id="empty string"
            ),
            pytest.param(
                "aba", False,
                id="not isogram with repeated characters"
            ),
            pytest.param(
                "moOse", False,
                id="not isogram with repeated characters"
            )
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
