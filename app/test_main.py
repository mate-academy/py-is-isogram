import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "", True,
                id="should return true with empty sting"
            ),
            pytest.param(
                "asdfg", True,
                id="should return true when a word has no repeating letters"
            ),
            pytest.param(
                "asdfgA", False,
                id=(
                    "should return False "
                    "when a word has repeating letters in different cases"
                )
            ),
            pytest.param(
                "asdffg", False,
                id=(
                    "should return false "
                    "when word has consecutive repeating letters"
                )
            ),
            pytest.param(
                "asdfgf", False,
                id=(
                    "should return false "
                    "when word has non-consecutive repeating letters"
                )
            ),
        ]
    )
    def test_should_return_correct_bool(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
