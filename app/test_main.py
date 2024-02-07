from app.main import is_isogram
import pytest


class TestIsIsonfram:
    @pytest.mark.parametrize(
        "word, boolian",
        [
            ("", True),
            ("look", False),
            ("Adam", False),
            ("playgrounds", True),
            (" ", True),
        ],
        ids=[
            "empy list is True",
            "empy list is True",
            "empy list is True",
            "empy list is True",
            "empy list is True",
        ]
    )
    def test_get_coin_comb(self, word: str, boolian: bool) -> None:
        assert is_isogram(word) is boolian

    @pytest.mark.parametrize(
        "word, error",
        [
            (1, AttributeError),
        ],
        ids=[
            "word must be str"
        ],
    )
    def test_errors_for_int_values(self,
                                   word: str,
                                   error: AttributeError) -> None:
        with pytest.raises(error):
            is_isogram(word)
