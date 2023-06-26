import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_word,result",
        [
            ("test", False),
            ("Test", False),
            ("MateAcademy", False),
            ("python", True),
            ("", True)
        ]
    )
    def test_should_check_properly(
            self,
            input_word: str,
            result: bool
    ) -> None:
        assert is_isogram(input_word) == result
