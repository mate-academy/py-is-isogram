import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "define",
                False,
                id="should return 'False'"
            ),
            pytest.param(
                "",
                True,
                id="should return 'True' if argument is empty"
            ),
            pytest.param(
                "x",
                True,
                id="should return 'True' if value is one letter"
            ),
            pytest.param(
                "xy",
                True,
                id="should return 'True'"
            ),
            pytest.param(
                "something",
                True,
                id="should return 'True'"
            ),
            pytest.param(
                "  ",
                False,
                id="double 'space' should return 'False'"
            ),
            pytest.param(
                "mEasure",
                False,
                id="should return 'False' "
                   "when uppercase and undercase letter"
            )
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
