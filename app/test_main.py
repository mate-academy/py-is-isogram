import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            (
                "play",
                True
            ),
            (
                "hello",
                False
            ),
            (
                "wonder",
                True
            ),
            (
                "",
                True
            ),
            (
                "lOok",
                False
            ),
            (
                "a b c",
                False
            )
        ]
    )
    def test_word_is_isogram(
        self,
        word: str,
        result: bool
    ) -> None:
        assert is_isogram(word) == result
