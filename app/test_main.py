import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "phrase, expected_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            (" ", True),
            ("  ", False),
        ],
        ids=[
            "should be True if phrase is isogram",
            "should be False if phrase have > 1 same letter",
            "should be False if phrase have > 1 same letter (big/small)",
            "should be True if phrase is empty",
            "should be True if phrase contain 1 space",
            "should be False if phrase contain more then 1 space",
        ]
    )
    def test_correct_combination(
            self,
            phrase: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(phrase) == expected_result
