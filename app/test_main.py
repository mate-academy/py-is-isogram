import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_value",
        [
            pytest.param("playgrounds", id="word should be isogram"),
            pytest.param("", id="empty string should be isogram")
        ]
    )
    def test_word_is_isogram(self,
                             input_value: str) -> None:
        result = is_isogram(input_value)
        assert result == True


class TestNotIsogram:
    @pytest.mark.parametrize(
        "input_value",
        [
            pytest.param('look', id="word don't should be isogram")
        ]
    )
    def test_word_is_not_isogram(self,
                                 input_value: str) -> None:
        result = is_isogram(input_value)
        assert result == False


class TestCaseInsensitive:
    @pytest.mark.parametrize(
        "input_value,expected_result",
        [
            pytest.param("Adam", False, id="Adam is not isogram")
        ]
    )
    def test_case_sense(self,
                        input_value: str,
                        expected_result: bool) -> None:
        result = is_isogram(input_value)
        assert result == expected_result
