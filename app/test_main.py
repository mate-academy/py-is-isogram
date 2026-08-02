import pytest
from _pytest.mark import ParameterSet

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_date, result",
        [
            pytest.param("playgrounds", True, id=(
                "Isogram - word that has no repeating letters"
            )
            ),
            pytest.param("", True, id=(
                "Empty string is an isogram"
            )
            ),
            pytest.param("Aa", False, id=(
                "String with different cases of"
                " the same letter is not an isogram"
            )
            ),
            pytest.param("ooooo", False, id=(
                "Not only consecutive letters are not an isogram."
            )
            ),
            pytest.param("orcrco", False, id=(
                "Not only non-consecutive letters are not an isogram."
            )
            ),
        ]
    )
    def test_correctly_check_isogram(
        self,
        input_date: ParameterSet,
        result: ParameterSet
    ) -> None:
        assert is_isogram(input_date) == result
