import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_string, expected_result",
        [
            pytest.param(
                "playgrounds", True,
                id="test should return True when word is 'playgrounds'"
            ),
            pytest.param(
                "look", False,
                id="test should return False when word is 'look'"
            ),
            pytest.param(
                "Adam", False,
                id="test should return False when word is 'Adam'"
            ),
            pytest.param(
                "", True,
                id="test should return True when word is ''"
            ),
        ]
    )
    def test_is_isogram(
            self,
            initial_string: str,
            expected_result: list[int]
    ) -> None:
        assert is_isogram(
            initial_string
        ) == expected_result
