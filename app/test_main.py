import pytest

from app.main import is_isogram


class TestIsIsogram:
    def test_invalid_param_type(self) -> None:
        with pytest.raises(AttributeError):
            is_isogram(1)

    def test_case_insensetive(self) -> None:
        assert is_isogram("AdEel") is False

    def test_empty_input_text(self) -> None:
        assert is_isogram("") is True

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
        ],
        ids=[
            "Word 'playgrounds' is isogram",
            "Word 'look' is not isogram",
            "Word 'Adam' is not isogram"
        ]
    )
    def test_expected_behavior(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
