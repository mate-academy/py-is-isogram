import pytest

from app.main import is_isogram


class TestIsogramFunc:
    @pytest.mark.parametrize(
        "initial_world, expected_bool",
        [
            (
                pytest.param(
                    "",
                    True,
                    id="should check an empty string as True"
                )
            ),
            (
                pytest.param(
                    "playgrounds",
                    True,
                    id="should check an long string"
                )
            ),
            (
                pytest.param(
                    "Adam",
                    False,
                    id="should be case-insensitive"
                )
            ),
            (
                pytest.param(
                    "look",
                    False,
                    id="should heck the string with consecutive letters"
                )
            )
        ]
    )
    def test_check_isogram_correctly(self,
                                     initial_world: str,
                                     expected_bool: bool) -> None:
        assert is_isogram(initial_world) == expected_bool
