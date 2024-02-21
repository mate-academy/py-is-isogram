import pytest
from app.main import is_isogram


class TestIsIsogramClass:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "parking",
                True,
                id="should check if it is an isogram"
            ),
            pytest.param(
                "BigWandw",
                False,
                id="should check two lower and upper case"
            ),
            pytest.param(
                "",
                True,
                id="should check empty string is a isogram"
            ),
            pytest.param(
                "nnnnnnn",
                False,
                id="should check non consecutive letters are not isogram"
            ),
        ]
    )
    def test_modify_class_correctly(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        result = is_isogram(word)

        assert result == expected_result
