from app.main import is_isogram
import pytest


class TestMain:
    @pytest.mark.parametrize("word, result", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ])
    def test_return_word_is_unique(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result

    def test_should_raise_type_error(self) -> None:
        with pytest.raises(TypeError):
            is_isogram(1)
