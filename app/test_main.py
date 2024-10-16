import pytest

from app.main import is_isogram

class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("downstream", True),
            ("Color", False)
        ]
    )
    def test_word_should_be_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            (1, AttributeError),
            (("word", ), AttributeError),
            (["look", "horror"], AttributeError),
            ({}, AttributeError)
        ]
    )
    def test_(self, word: any, expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)

