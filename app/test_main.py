import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_str, result",
        [
            pytest.param(
                "",
                True,
                id="Should return `True` for empty string"
            ),
            pytest.param(
                "abcdefghijklmnopqrstuvwxyz",
                True,
                id="Should return `True` for unique lowercase letters"
            ),
            pytest.param(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                True,
                id="Should return `True` for unique uppercase letters"
            ),
            pytest.param(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                False,
                id=("Should return `False` for repeating letters with "
                    "different case"),
            ),
            pytest.param(
                "Madagascar",
                False,
                id=("Should return `False` for word with non-consecutive "
                    "repeating letters"),
            ),
            pytest.param(
                "WatTer",
                False,
                id=("Should return `False` for word with repeating letters "
                    "different case"),
            ),
            pytest.param(
                "k",
                True,
                id="Should return `True` for single letter"
            ),
            pytest.param(
                "k" * 100,
                False,
                id=("Should return `False` for repeating single letter "
                    "multiple times"),
            ),
        ],
    )
    def test_is_isogram(self, input_str: str, result: bool) -> None:
        assert is_isogram(input_str) == result
