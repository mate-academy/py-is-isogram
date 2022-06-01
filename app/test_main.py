import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, bool_result",
        [
            pytest.param(
                "",
                True,
                id="Should return True, when word is empty"),
            pytest.param(
                "Elephant",
                False,
                id="Should be case-insensitive"),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False)
        ]
    )
    def test_is_isogram_should_return_correct_bool(self, word, bool_result):
        assert is_isogram(word) == bool_result, (
            f"Function 'is_isogram' should return {bool_result} "
            f"when 'word' equals to {word}"
        )
