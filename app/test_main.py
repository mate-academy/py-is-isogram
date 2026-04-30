import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize("word, expected",
                             [
                                 ("", True),
                                 ("A", True),
                                 ("playgrounds", True),
                                 ("True", True),
                                 ("Hello", False),
                                 ("crossroads", False),
                                 ("Consecutive", False),
                                 ("noNe", False),
                                 ("ANONYMOUS", False)
                             ])
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
