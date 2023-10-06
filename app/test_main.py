import pytest

from app.main import is_isogram


class TestIsIsogramClass:

    @pytest.mark.parametrize(
        "word, value",
        [
            ("", True),
            ("Adam", False),
            ("look", False),
            ("playgrounds", True),
            ("loOk", False)

        ]
    )
    def test_is_isogram_values(self, word: str, value: bool) -> None:

        assert is_isogram(word) is value
