import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_boolean",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_return_boolean_value(word: str, expected_boolean: bool) -> None:
    assert is_isogram(word) == expected_boolean
