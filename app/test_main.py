import pytest

from app.main import is_isogram


class TestTask:
    @pytest.mark.parametrize(
        "value, expected_result",
        [
            pytest.param(
                "",
                True,
                id="empty string should return True"
            ),
            pytest.param(
                "AbCd",
                True,
                id="Should return True"
            ),
            pytest.param(
                "Aa",
                False,
                id="Should ignore type of camel style and return False"
            ),
            pytest.param(
                "Aba",
                False,
                id="Should ignore type of camel style and return False"
            )
        ]
    )
    def test_words(self, value, expected_result):
        assert is_isogram(value) == expected_result
