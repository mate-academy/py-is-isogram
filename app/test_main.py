from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param("playgrounds",
                         True,
                         id="test long word"),
            pytest.param("look",
                         False,
                         id="test word with consecutive letters"),
            pytest.param("chocolate",
                         False,
                         id="test word with nonconsecutive letters"),
            pytest.param("",
                         True,
                         id="test empty word"),
        ]

    )
    def test_correct_answer(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result

    def test_only_letters(self) -> None:
        assert is_isogram("abcde123") is False
