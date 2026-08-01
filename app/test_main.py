import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        ("word", "result"),
        [
            pytest.param("kindergarten", False, id="kindergarten word"),
            pytest.param("vision", False, id="vision word"),
            pytest.param("breach", True, id="breach word"),
            pytest.param("cat", True, id="cat word"),
            pytest.param("Agenda", False, id="case-insensitive Agenda word"),
            pytest.param("", True, id="blank space"),
        ]
    )
    def test_should_return_if_word_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
