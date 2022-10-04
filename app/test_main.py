import pytest


from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playground",
                True,
                id="should return True if word == 'playground'"
            ),
            pytest.param(
                "look",
                False,
                id="should return False if word == 'look'"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return False if word == 'Adam'"
            ),
            pytest.param(
                "",
                True,
                id="should return True if word == ''"
            )
        ]
    )
    def test_if_is_isogram_works_correctly(
        self,
        word,
        expected_result
    ):
        assert is_isogram(word) == expected_result
