import pytest

from app.main import is_isogram

class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "",
                True,
                id="the empty string is an isogram"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="word 'playground' has no repeating letters"
            ),
            pytest.param(
                "look",
                False,
                id="word 'look' has repeating 'o'"
            ),
            pytest.param(
                "Adam",
                False,
                id="word 'Adam' ha repeating 'a' in lower and upper case"
            ),
            pytest.param(
                "Python",
                True,
                id="word 'Python' has no repeating letters"
            ),
            pytest.param(
                "Mirror",
                False,
                id="word 'Mirror' has repeating 'r'"
            ),
            pytest.param(
                "Processor",
                False,
                id="word 'Mirror' has repeating 's'"
            ),
            pytest.param(
                "Cup",
                True,
                id="word 'Cup' has no repeating letters"
            ),
            pytest.param(
                "pytest",
                False,
                id="word 'pytest' has repeating 't'"
            )
        ]
    )
    def test_cat_and_dog_years(
            self,
            word: int,
            expected_result: list
    ) -> None:
        assert is_isogram(word) == expected_result
