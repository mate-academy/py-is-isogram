import pytest

from app.main import is_isogram


class TestIsogram:

    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param("playgrounds", True, id="should valid isogram"),
            pytest.param("look", False, id="should valid isogram"),
            pytest.param("Adam", False, id="should valid isogram"),
            pytest.param("", True, id="should valid isogram")
        ]
    )
    def test_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected


class TestIsogramErrors:
    @pytest.mark.parametrize(
        "word, expected_error",
        [
            pytest.param(12, TypeError, id="should raise if Not string"),
            pytest.param("type ", TypeError, id="should raise if Not letter"),
        ]
    )
    def test_isogram_errors(
            self, word: str, expected_error: type[TypeError]
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
