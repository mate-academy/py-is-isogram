import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize("word: str, expected_value: bool", [
        ("playgrouds", True),
        ("Look", False),
        ("Adam", False),
        ("Alfa", False),
        ("Mate", True),
        ("brother", False),
        ("Chemistry", True)
    ])
    def test_is_isogram(self,
                        word: str,
                        expected_value: bool
                        ) -> None:
        assert is_isogram(word) == expected_value
