from pickle import FALSE  # noqa F401

from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "init_str,expected_bool",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return true for playgrounds",
            ),
            pytest.param(
                "look",
                False,
                id="should return false for look",
            ),
            pytest.param(
                "Adam",
                False,
                id="should return false for Adam",
            ),
            pytest.param(
                "",
                True,
                id="should return true for empty string",
            ),
        ]
    )
    def test_is_isogram(self, init_str: str, expected_bool: bool) -> None:
        assert is_isogram(init_str) == expected_bool
