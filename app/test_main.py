from app.main import is_isogram
import pytest


class TestValues:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Test should return True for 'playgrounds'"),
            pytest.param(
                "look",
                False,
                id="Test should return True for 'look'"),
            pytest.param(
                "Adam",
                False,
                id="Test should return False for 'Adam'"),
            pytest.param(
                "",
                True,
                id="Test should return True for '' "),
        ]
    )
    def test_common_values(self, word: str, expected_result: str) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "word, expected_error",
        [
            pytest.param(
                1,
                AttributeError,
                id="Test should return TypeError for integer"),
        ]
    )
    def test_attribute_error(self,
                             word: str,
                             expected_error: Exception) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
