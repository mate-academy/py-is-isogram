import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("playground", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("Playground", True)
        ],
    )
    def test_is_isogram(self,
                        word: str,
                        result: bool
                        ) -> None:
        assert is_isogram(word) == result
