import pytest

from app.main import is_isogram


def test_is_isogram_should_return_boolean() -> None:
    assert isinstance(is_isogram("abc"), bool)


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "", True,
                id="should return true for empty string"
            ),
            pytest.param(
                "test", False,
                id="should return false for non-consecutive duplicate"
            ),
            pytest.param(
                "look", False,
                id="should return false for consecutive duplicate"
            ),
            pytest.param(
                "Adam", False,
                id="should return false for capitalized duplicate"
            ),
            pytest.param(
                "bananas", False,
                id="should return false for triplet and duplicate"
            ),
            pytest.param(
                "playgrounds", True,
                id="should return true for 'isogram'"
            ),
        ]
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
