import pytest
from app.main import is_isogram


class TestWordIsogram:
    @pytest.mark.parametrize(
        "word,boolean",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should be isogram if all letters are different",
            ),
            pytest.param(
                "",
                True,
                id="should be isogram if is an empty string",
            ),
        ],
    )
    def test_should_be_isogram(self, word: str, boolean: bool) -> None:
        assert is_isogram(word) == boolean


class TestWordNotIsogram:
    @pytest.mark.parametrize(
        "word,boolean",
        [
            pytest.param(
                "look",
                False,
                id="should not to be isogram if there more than 1 same letter",
            ),
            pytest.param(
                "Adam",
                False,
                id="should be case sensitive",
            ),
        ],
    )
    def test_should_not_to_be_isogram(self, word: str, boolean: bool) -> None:
        assert is_isogram(word) == boolean
