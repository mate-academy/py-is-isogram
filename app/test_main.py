import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_isogram_check_result",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("aAbB", False),
    ]
)
def test_isogram(
        word: str,
        expected_isogram_check_result: bool
) -> None:
    assert is_isogram(word) == expected_isogram_check_result
