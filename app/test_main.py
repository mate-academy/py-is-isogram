import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word_to_check, expected_boolean_value",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("world", True),
        ("hello", False),
        ("Tunel", True),
        ("Bottle", False),
    ]
)
def test_is_isogram(word_to_check: str, expected_boolean_value: bool) -> None:
    assert is_isogram(word_to_check) == expected_boolean_value
