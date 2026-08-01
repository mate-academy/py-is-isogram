import pytest

from app.main import is_isogram


class TestForWorking:
    @pytest.mark.parametrize(
        "word,expected",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("porcelain", True)
        ]
    )
    def test_for_correct_result(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected


class TestForErrors:
    def test_for_non_string(self) -> None:
        with pytest.raises(TypeError):
            is_isogram(12345)
