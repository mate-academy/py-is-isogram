import pytest
from app.main import is_isogram


class TestPositiveCases:
    @pytest.mark.parametrize(
        "word",
        [
            "",
            "a",
            "playgrounds",
            "Dermatoglyphics",
            "qwerty",
            "isogram",
            "background",
            "lumberjacks",
            "thumbscrewjapingly",
            "sixyearold",
        ],
    )
    def test_should_return_true_for_isograms(self, word: str) -> None:
        assert is_isogram(word) is True


class TestNegativeCases:
    @pytest.mark.parametrize(
        "word",
        [
            "look",
            "Adam",
            "aba",
            "Alphabet",
            "moOse",
            "moSeQuiTo",  # ✅ тут йому правильне місце
            "Letter",
            "Aa",
            "BbB",
        ],
    )
    def test_should_return_false_for_non_isograms(self, word: str) -> None:
        assert is_isogram(word) is False


class TestCaseInsensitivity:
    @pytest.mark.parametrize(
        "word",
        [
            "Aba",
            "moOse",
            "Letter",
            "Aa",
            "BbB",
        ],
    )
    def test_should_ignore_case(self, word: str) -> None:
        assert is_isogram(word) is False


class TestEdgeCases:
    def test_single_letter_is_isogram(self) -> None:
        assert is_isogram("x") is True

    def test_empty_string_is_isogram(self) -> None:
        assert is_isogram("") is True

    def test_return_type_should_be_bool(self) -> None:
        result = is_isogram("test")
        assert isinstance(result, bool)
