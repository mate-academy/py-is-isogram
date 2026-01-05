from app.main import is_isogram
import pytest


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="word is isogram",
            ),
            pytest.param(
                "look",
                False,
                id="word is not isogram",
            ),
            pytest.param(
                "Adam",
                False,
                id="word has bif and small the same letter is isogram",
            ),
            pytest.param(
                "",
                True,
                id="word empty and is_isogram",
            ),
        ]
    )
    def test_is_isogram_correctly(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            pytest.param(
                [],
                AttributeError,
                id="should raise error when arg is list",
            )
        ]
    )
    def test_should_raise_error_correctly(
        self,
        word: str,
        expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            assert is_isogram(word)
