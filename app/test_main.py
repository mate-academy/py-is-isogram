import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "input_string, expected_output",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return true with isogram"
            ),
            pytest.param(
                "look",
                False,
                id="should return false with consecutive repeting letters"
            ),
            pytest.param(
                "letter",
                False,
                id="should return false with non-consecutive repeating words"
            ),
            pytest.param(
                "",
                True,
                id="should return true if empty string"
            ),
            pytest.param(
                "Adam",
                False,
                id="should work correct with different registers"
            )
        ]
    )
    def test_works_correct(self, input_string, expected_output):
        compare = is_isogram(input_string)
        assert compare == expected_output
