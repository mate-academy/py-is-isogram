import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param
            (
                "Adam",
                False,
                id="String with different cases"
                   " of the same letter is not an isogram"
            ),
            pytest.param
            (
                "",
                True,
                id="Empty string is an isogram"
            ),
            pytest.param
            (
                "look",
                False,
                id="Not only consecutive letters are not an isogram"
            ),
        ]
    )
    def test_is_isogram_should_return_correct_value(self,
                                                    word,
                                                    expected):
        assert is_isogram(word) == expected
