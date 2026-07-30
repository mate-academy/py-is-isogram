import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize("word,expected", [
        pytest.param(
            "playgrounds",
            True,
            id="returns True for 'playgrounds'"
        ),
        pytest.param(
            "look",
            False,
            id="returns False for 'look'"
        ),
        pytest.param(
            "Adam",
            False,
            id="returns False for 'Adam'"
        ),
        pytest.param(
            "",
            True,
            id="returns True for ''"
        ),
        pytest.param(
            "six-year-old",
            False,
            id="returns False for 'six-year-old'"
        ),
        pytest.param(
            "Subdermatoglyphic",
            True,
            id="returns True for 'Subdermatoglyphic'"
        ),
        pytest.param(
            "Adam",
            False,
            id="returns True for 'Adam'"
        ),
    ])
    def test_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
