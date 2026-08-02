import pytest
from app import main


class TestCorrectlyDefinitiesIsogram:

    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("a", True),
            ("aa", False),
            ("", True),
            ("abcde" * 10, False),
            ("AbCdEfGhIj", True),
            ("isogram", True),
            ("Dermatoglyphics", True),
            ("SENIOR", True),
            ("33", False),
            ("1234567890", True)
        ],
    )
    def test_converts_ages_correctly(
        self,
        word: str,
        result: bool
    ) -> None:
        assert main.is_isogram(word) == result

    @pytest.mark.parametrize(
        "word",
        [
            (12),
            (3.14),
            ([]),
            (False),
            ({})
        ],
    )
    def test_raises_type_error_for_non_str_values(
        self,
        word: str
    ) -> None:
        with pytest.raises(TypeError):
            main.is_isogram(word)
