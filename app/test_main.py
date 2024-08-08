import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected", [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            pytest.param("", True, id="empty string")
        ]
    )
    def test_is_isogram_valid(self, word: str, expected: bool) -> None:
        assert (is_isogram(word) == expected
                ), f"Result for {word} must be {expected}"

    @pytest.mark.parametrize("word", [True, 3, None, 5.5])
    def test_is_isogram_type(self, word: str) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
