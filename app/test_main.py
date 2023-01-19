import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_bool",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("adam", False),
            ("", True)
        ]
    )
    def test_is_a_word_isogram(
            self,
            word: str,
            expected_bool: bool
    ) -> None:
        assert is_isogram(word) == expected_bool


def test_receives_an_incorrect_type() -> None:
    with pytest.raises(AttributeError):
        is_isogram(15)
