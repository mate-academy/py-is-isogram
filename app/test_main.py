import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_bool",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_modify_classes_correctly(
            self,
            word: str,
            expected_bool: bool
    ) -> None:

        assert is_isogram(word) == expected_bool
