import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_error",
        [
            pytest.param(
                10,
                AttributeError,
                id="should raise TypeError when word != str"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            word: str,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)

    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "",
                True,
                id="should return True if word is empty string"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="should return True if isogram word presented"
            ),
            pytest.param(
                "loOk",
                False,
                id="should return False if word have repeating letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return False if word have repeating"
            )
        ]
    )
    def test_word_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
