import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param("playgrounds", True,
                         id="'playgrounds' is a isogram"),
            pytest.param("look", False,
                         id="'look' is not a isogram"),
            pytest.param("Adam", False,
                         id="'Adam' is a isogram"),
            pytest.param("", True,
                         id="'' is a isogram")
        ]
    )
    def test_is_isogram_with_correct_args(self,
                                          word: str,
                                          result: bool) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "not_word",
        [
            pytest.param(1),
            pytest.param([12, 4]),
            pytest.param((12,))
        ]
    )
    def test_is_isogram_with_incorrect_args(self,
                                            not_word: str) -> None:
        with pytest.raises(AttributeError):
            assert is_isogram(not_word)
