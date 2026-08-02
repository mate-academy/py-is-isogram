import pytest

from app.main import is_isogram


class TestCoinCombination:
    def test_should_check_non_str_argument(self) -> None:
        with pytest.raises(AttributeError):
            is_isogram(100)

    @pytest.mark.parametrize(
        "isogram,expected_result",
        [
            pytest.param(
                "",
                True,
                id="checking, that the empty string should be isogram"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="checking correct result"
            ),
            pytest.param(
                "look",
                False,
                id="checking case-independent repetition"
            ),
            pytest.param(
                "Adam",
                False,
                id="checking case-sensitive repetition"
            )
        ]
    )
    def test_should_return_correct_list(
            self, isogram: str, expected_result: bool) -> None:
        assert is_isogram(isogram) == expected_result
