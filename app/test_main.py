import pytest
from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "string,result",
        [
            pytest.param("", True,
                         id="test empty string is isogram"),
            pytest.param("look", False,
                         id="test false if letters repeated"),
            pytest.param("Adam", False,
                         id="test case-insensitive "),
            pytest.param("qwerty", True,
                         id="test isogram is true"),
            pytest.param("qwert yuiop", True,
                         id="test sentence with one space"),
            pytest.param(" qwert yuiop ", False,
                         id="test multiple spaces"),
        ]
    )
    def test_isogram(self, string: str, result: bool) -> None:
        assert is_isogram(string) == result

    @pytest.mark.parametrize(
        "wrong_value,error",
        [
            pytest.param((45, [4, 5], {}), AttributeError,
                         id="test wrong data input"),
        ]
    )
    def test_incorrect_input(self,
                             wrong_value: tuple,
                             error: Exception) -> None:
        for value in wrong_value:
            with pytest.raises(error):
                is_isogram(value)
