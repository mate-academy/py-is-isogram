import pytest

from app.main import is_isogram


@pytest.mark.parametrize("check_word, bool_res", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True)
])
def test_get_upper_lower_mixed_empty_value(check_word: str,
                                           bool_res: bool) -> None:
    assert is_isogram(check_word) == bool_res
