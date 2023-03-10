import pytest


from app.main import is_isogram


class TestCheckWord:
    @pytest.mark.parametrize(
        "word,result_test",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should be isogram"
            ),
            pytest.param(
                "look",
                False,
                id="should be not isogram"
            ),
            pytest.param(
                "Adam",
                False,
                id="should be not isogram"
            ),
            pytest.param(
                "",
                True,
                id="should be isogram"
            )
        ]
    )
    def test_word_is_isogram(
            self,
            word: str,
            result_test: bool
    ) -> None:
        assert is_isogram(word) == result_test
