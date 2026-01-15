import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ],
        ids=[
            "Should return True when word is 'playgrounds'",
            "Should return False when word is 'look'",
            "Should return False when word is 'Adam'",
            "Should return True when word is ''",
        ]
    )
    def test_word_if_isogram(
        self,
        word: str,
        result: bool
    ) -> None:
        assert (
            is_isogram(word) == result
        ), "Should return bool value when value is given"
