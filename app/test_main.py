import pytest

from app.main import is_isogram

# write your code here
@pytest.mark.parametrize(
    "word,expected_bool",
    [
        (
            "playgrounds",
            True
        ),
        (
            "look",
            False
        ),
        (
            "Adam",
            False
        ),
        (
            "",
            True
        ),
    ]
)
def test_should_check_isogram_correctly(
        word: str,
        expected_bool: bool,
) -> None:
    assert is_isogram(word) == expected_bool