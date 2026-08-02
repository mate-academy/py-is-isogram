import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                '',
                True,
                id="empty string"
            ),
            pytest.param(
                'adAm',
                False,
                id="uppercase and lowercase"
            ),
            pytest.param(
                'playgrounds',
                True,
                id="is isogram true"
            ),
            pytest.param(
                'look',
                False,
                id="adjacent letters"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word,
            expected_result
    ):
        assert is_isogram(word) == expected_result
