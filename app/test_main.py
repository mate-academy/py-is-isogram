import pytest

from app.main import is_isogram


class TestIsIsogramClass:
    @pytest.mark.parametrize(
        "check_word, result",
        [
            pytest.param('playgrounds',
                         True,
                         id="this is an isogram"),
            pytest.param("look",
                         False,
                         id="this is not an isogram"),
            pytest.param("Adam",
                         False,
                         id="this is not an isogram"),
            pytest.param("",
                         True,
                         id="an empty value is an isogram")
        ]
    )
    def test_to_check_isogram(
            self,
            check_word: str,
            result: bool
    ) -> None:
        assert is_isogram(check_word) == result
