import pytest
from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ],
        ids=[
            "with long word",
            "with double 'o'",
            "with a capital letter",
            "with empty string"
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert (
            is_isogram(word) == result
        ), f"Word {word} should be equal {result} "
