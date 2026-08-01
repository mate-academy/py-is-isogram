from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, exp",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
class TestCase:
    def test_is_isogram(self, word: str, exp: bool) -> None:
        assert is_isogram(word) == exp

    def test_word_is_string(self, word: str, exp: bool) -> None:
        assert isinstance(word, str)


class TestEdgeCase:
    def test_word_is_int_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            is_isogram(2025)

    def test_word_is_none_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            is_isogram(None)
