import pytest


from app.main import is_isogram


class TestIsogramCheck:
    @pytest.mark.parametrize(
        "value, result",
        [
            pytest.param(
                "",
                True,
                id="Should return True if empty string"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="Should return True if string is isogram"
            ),
            pytest.param(
                "letter",
                False,
                id="Should return False if letters are consecutive"
            ),
            pytest.param(
                "Test",
                False,
                id="Should be case-insensitive and non-consecutive"
            )
        ]
    )
    def test_func_works_correctly(
            self,
            value: str,
            result: bool
    ) -> None:
        assert is_isogram(value) == result
