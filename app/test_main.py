import pytest

from app.main import is_isogram


class TestFunctionWorksCorrectly:
    @pytest.mark.parametrize(
        "data,returned",
        [
            pytest.param(
                "Adam",
                False,
                id="Function should be case-insensitive"
            ),
            pytest.param(
                "",
                True,
                id="Function should be return `True` when string empty"
            ),
            pytest.param(
                "playground",
                True,
                id="Function should be return `True` for `playground`"
            ),
            pytest.param(
                "look",
                False,
                id="Function should be return `False` for `look`"
            )
        ]
    )
    def test_func(self, data: str, returned: bool) -> None:
        assert is_isogram(data) is returned
