import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_word, expected_isogram_bool",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("They", True),
            ("Moment", False),
            ("Yer", True),
        ],
        ids=[
            "word-'playgrounds' bool-True",
            "word-'look' bool-False",
            "word-'Adam' bool-False",
            "word-'' bool-True",
            "word-'They' bool-True",
            "word-'Moment' bool-False",
            "word-'Yer' bool-True"
        ]
    )
    def test_modify_animals_age_correctly(
            self, input_word: str, expected_isogram_bool: bool
    ) -> None:
        assert is_isogram(input_word) == expected_isogram_bool
