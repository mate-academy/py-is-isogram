import pytest
from app.main import is_isogram


class TestIsIsogram():
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds", True,
                id="should return True for 'playgrounds'"
            ),
            pytest.param(
                "look", False,
                id="should return False for 'look' - o is repeated"
            ),
            pytest.param(
                "Adam", False,
                id="should return False for 'Adam' - A and a are repeated"
            ),
            pytest.param(
                "QqWEeRTy", False,
                id="should return False for 'QqWEeRTy' - "
                   "Qq and Ee are repeated"
            ),
            pytest.param(
                "QWERTYY", False,
                id="should return False for 'QWERTYY' - Y is repeated"
            ),
            pytest.param(
                "", True,
                id="should return True for empty string"
            ),
            pytest.param(
                " ", True,
                id="should return True for space"
            ),
            pytest.param(
                "  ", False,
                id="should return False for 2 spaces"
            ),
            pytest.param(
                "   ", False,
                id="should return Fasle for tab - spaces are repeated 4 times"
            ),
            pytest.param(
                "\n", True,
                id="should return True for new line"
            ),
            pytest.param(
                "\n\n", False,
                id="should return Flase for 2 new lines"
            ),
            pytest.param(
                " -", True,
                id="should return True for ' -'"
            ),
            pytest.param(
                " - ", False,
                id="should return False for ' - ' - space is repeated"
            ),
            pytest.param(
                " -%^#$!()?><", True,
                id="should return True for ' -%^#$!()?><'"
            ),
            pytest.param(
                "1234567890", True,
                id="should return True for '1234567890'"
            ),
            pytest.param(
                "1 -2,3,456789", False,
                id="should return False for '1 -2,3,456789' - "
                   "comma is repeated"
            ),
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
