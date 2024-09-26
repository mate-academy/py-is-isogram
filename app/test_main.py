import pytest
from typing import Any
from app.main import is_isogram


class TestIsogram:

    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param("elephant", False, id="isogram False"),
            pytest.param("word", True, id="isogram True"),
            pytest.param("Radar", False, id="isogram upper and lower"),
            pytest.param("", True, id="isogram empty string"),
            pytest.param("letter", False, id="isogram two letters in a row"),
            pytest.param("tt", False, id="double letter")
        ]
    )
    def test_isogram(
        self,
        word: str,
        result: bool
    ) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(12, id="word = integer"),
            pytest.param([], id="word = list"),
            pytest.param({}, id="word = dict"),
        ]
    )
    def test_isogram_error(
        self,
        word: Any
    ) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
