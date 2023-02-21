import pytest


from app.main import is_isogram


class TestIsogramCheck:
    @pytest.mark.parametrize(
        "string, result",
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
                id="Should be case-insensitive"
            ),
            pytest.param(
                "grogu",
                False,
                id="Should return False if letters are non-consecutive"
            )
        ]
    )
    def is_func_works_correctly(
            self,
            string: str,
            result: bool
    ) -> None:
        assert is_isogram(string) is result
