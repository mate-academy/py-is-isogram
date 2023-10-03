import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_str, expected_result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("PopPoOpP", False)
    ],
    ids=[
        "empty string",
        "word with non-repeating letters",
        "word with repeating letters",
        "sentence case word",
        "repeating letters in different case"
    ]
)
def test_is_isogram(
        input_str: str,
        expected_result: bool
) -> None:
    assert is_isogram(input_str) == expected_result
