import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param(
                "Tent",
                False,
                id="should be insensitive to case"
            ),
            pytest.param(
                "",
                True,
                id="should return True for empty str"
            ),
            pytest.param(
                "Park",
                True,
                id="should return True if isogram"
            ),
        ],
    )
    def test_is_isogram(self, word: str, expected: str) -> None:
        assert is_isogram(word) == expected
