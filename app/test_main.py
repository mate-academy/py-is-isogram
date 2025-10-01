from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param("lOok", False),
            pytest.param("Adam", False),
            pytest.param("avocado", False),
            pytest.param("Mate", True),
            pytest.param("python", True),
            pytest.param("", True)
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected

    def test_is_bool(self) -> None:
        assert isinstance(is_isogram("lOok"), bool)
