import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "entry_string, expected_output",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should check all lowercase and return True"
            ),
            pytest.param(
                "look",
                False,
                id="should check all lowercase and return False"
            ),
            pytest.param(
                "Flower",
                True,
                id="should check capitalized and return True"
            ),
            pytest.param(
                "Adam",
                False,
                id="should check capitalized and return False"
            ),
            pytest.param(
                "fLoWer",
                True,
                id="should check mixed casing and return True"
            ),
            pytest.param(
                "MiSsinG",
                False,
                id="should check mixed casing and return False"
            ),
            pytest.param(
                "",
                True,
                id="should check empty string and return True"
            ),
        ]
    )
    def test_correct_assessment_if_isogram(
            self,
            entry_string: str,
            expected_output: bool
    ) -> None:
        assert is_isogram(entry_string) == expected_output
