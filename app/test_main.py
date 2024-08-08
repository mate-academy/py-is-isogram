import pytest
from app.main import is_isogram

# write your code here


class TestMainApp:
    @pytest.mark.parametrize(
        "initial_string,expected_result",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
        ],
        ids=[
            "When string is empty must be True",
            "When string is isogram must be True",
            "When string is not isogram must be False",
            "When string have 2 same but 1 capital letter must be False",
        ]
    )
    def test_correct(
            self,
            initial_string: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(initial_string) == expected_result

    @pytest.mark.parametrize(
        "initial_string,expected_error",
        [
            pytest.param(
                1,
                AttributeError,
                id="Initial value must be string"
            ),
        ],
    )
    def test_incorrect(
            self,
            initial_string: str,
            expected_error: str
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(initial_string)
