import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_value",
        [
            pytest.param(
                'playgrounds',
                True,
                id="should return True"
            ),
            pytest.param(
                'look',
                False,
                id="should return False"
            ),
            pytest.param(
                'Adam',
                False,
                id="should return False"
            ),
            pytest.param(
                '',
                True,
                id="should return True"
            ),
        ]
    )
    def test_is_isogram(self, word: str, expected_value: bool):
        assert is_isogram(word) == expected_value
