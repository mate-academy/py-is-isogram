from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param("playgrounds", True,
                         id="valid isogram"),
            pytest.param("look", False,
                         id="not isogram repeated o"),
            pytest.param("Adam", False,
                         id="not isogram case insensitive"),
            pytest.param("", True,
                         id="empty string is isogram"),
        ],
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(123, id="non_string_input"),
        ],
    )
    def test_should_raise_error_if_not_type_str(self, word: str) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
