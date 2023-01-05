import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_return_correct_values(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word",
        [
            (12),
            (["look"]),
            (True)
        ]
    )
    def test_receive_correct_value_type(
            self,
            word: str,
    ) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
