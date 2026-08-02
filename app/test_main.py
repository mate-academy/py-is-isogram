import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("", True),
            ("Adam", False),
            ("playgrounds", True),
            ("look", False)
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            25,
            25.7534,
            ("sgsdg",),
            None,
            [25],
            {"cents": 25},
        ]
    )
    def test_is_isogram_invalid_input(
            self,
            invalid_input: Exception
    ) -> None:
        with pytest.raises(Exception):
            is_isogram(invalid_input)
