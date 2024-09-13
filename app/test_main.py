import pytest

from app.main import is_isogram


class TestIsIsogramClass:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("pLaYgRoUnDs", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert (
            is_isogram(word) == result
        ), f"{is_isogram(word)} should return {result}"


class TestIsIsogramError:
    def test_if_isogram_take_int_param(self) -> None:
        with pytest.raises(AttributeError):
            is_isogram(12)
