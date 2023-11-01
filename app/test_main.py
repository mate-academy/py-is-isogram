import pytest

from app.main import is_isogram

# write your code here
class TestIsIsogramFunc:
    @pytest.mark.parametrize(
        "string, result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
            ("cHupaChups", False),
            ("Hello", False),
        ]
    )
    def test_is_isogram_func(
            self,
            string: str,
            result: bool
    ) -> None:
        assert is_isogram(string) is result

    def test_correct_type(self) -> None:
        with pytest.raises(AttributeError):
            is_isogram(123)