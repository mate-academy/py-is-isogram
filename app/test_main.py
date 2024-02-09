import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expended",
        [
            pytest.param(
                "playgrounds", True,
                id="all letters are unique"
            ),
            pytest.param(
                "look", False,
                id="two letters are repeated"
            ),
            pytest.param(
                "Adam", False,
                id="capital letter and small letter are repeated"
            ),
            pytest.param(
                "", True,
                id="empty string"
            )
        ]
    )
    def test_is_isogram(self, word: str, expended: bool) -> None:
        assert is_isogram(word) == expended
