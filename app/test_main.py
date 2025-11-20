from app.main import is_isogram
import pytest


class TestMain:
    @pytest.mark.parametrize("word, result_bool", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ])
    def test_should_return_word_without_repetitions(self, word: str, result_bool: bool) -> None:
        assert is_isogram(word) == result_bool

    def test_should_raise_type_error(self) -> None:
        with pytest.raises(TypeError):
            is_isogram(1)
