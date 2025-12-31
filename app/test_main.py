import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("  ", False)
    ]
)
def test_should_check_all_cases(input_word: str, expected: bool) -> None:
    assert is_isogram(input_word) is expected
