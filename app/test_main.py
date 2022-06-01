import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, bool_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            pytest.param("", True, id="Should return True, when word is empty")
        ]
    )
    def test_is_isogram_should_return_correct_bool(self, word, bool_result):
        assert is_isogram(word) == bool_result, (
            f"Function 'is_isogram' should return {bool_result} "
            f"when 'word' equals to {word}"
        )
