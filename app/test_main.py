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
            "should return True if each letter in phrase occurs the same number of times",
            "should return False if phrase have more then 1 same letter",
            "should return False if phrase have more then 1 same letter (big or small)",
            "should return True if phrase is empty",
            "should return True if phrase contain 1 space",
            "should return False if phrase contain more then 1 space",
        ]
    )
    def test_correct_combination(
            self,
            phrase: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(phrase) == expected_result
