import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("1234", True),
            ("", True)
        ]
    )
    def test_input_word(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(1, id="input 'int' type"),
            pytest.param({"": "123"}, id="input 'dict' type", ),
            pytest.param((1, 2, 3, 4), id="input 'tuple' type")

        ]
    )
    def test_unexpected_type(self, word: any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
