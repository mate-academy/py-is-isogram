import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("computer", True),
            ("Adam", False),
            ("book", False),
            ("beak", True),
            (" ", True),
            ("", True)
        ]
    )
    def test_should_correctly_detect_isograms(
        self,
        word: str,
        result: bool
    ) -> None:
        assert is_isogram(word) == result
