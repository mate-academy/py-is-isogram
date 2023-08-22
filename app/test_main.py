import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string, expected_result",
        [
            pytest.param(
                "playgrounds", True, id="should return true if isogram"
            ),
            pytest.param(
                "look", False, id="should return false if not isogram"
            ),
            pytest.param(
                "", True, id="should return true if empty str"
            ),
            pytest.param(
                "AbraciB", False, id="should be case-insensitive "
            )
        ]
    )
    def test_should_return_correct_answer(
            self,
            string: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(string) == expected_result

    def test_should_return_bool(self) -> None:
        assert isinstance(is_isogram(""), bool)
