import pytest

from app.main import is_isogram


class TestWord:
    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ]
    )
    def test_correct_checks_of_the_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result


def test_not_string_type_exception() -> None:
    with pytest.raises(AttributeError):
        is_isogram(99)
