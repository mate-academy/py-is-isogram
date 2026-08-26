import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("playground", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("ABCDEFGHIJKLMNOP", True),
            ("aaabbbccc", False),
            ("12345", True)
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "input_text, expected_error",
        [
            (124120, AttributeError),
            (True, AttributeError),
            (None, AttributeError)
        ]
    )
    def test_is_isogram_errors(
            self,
            input_text: int | bool | None,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(input_text)
