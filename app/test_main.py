import pytest

from app.main import is_isogram


class TestIsIsogram:

    def test_is_isogram_return_bool(self) -> None:
        assert isinstance(is_isogram("Array"), bool)

    @pytest.mark.parametrize(
        "word, expected",
        [
            ("look", False),
            ("playgrounds", True),
            ("Adam", False),
            ("Array", False),
            ("talk", True),
            ("", True),
        ]
    )
    def test_is_isogram_correct_return(self,
                                       word: str,
                                       expected: bool) -> None:
        assert is_isogram(word) == expected, (
            f"Expected {expected}, got {is_isogram(word)}"
        )
