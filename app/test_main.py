from app.main import is_isogram

from pytest import mark, param


class TestModify:
    @mark.parametrize(
        "word, result",
        [
            param(
                "playgrounds",
                True,
                id="ErrorWord: playgrounds"
            ),
            param(
                "look",
                False,
                id="ErrorWord: look"
            ),
            param(
                "Adam",
                False,
                id="ErrorWord: Adam"
            ),
            param(
                "",
                True,
                id="ErrorWord: empty line"
            ),
        ]
    )
    def test_modify(self, word: str, result: bool) -> None:
        assert isinstance(word, str), "Please enter a string"
        assert is_isogram(word) == result