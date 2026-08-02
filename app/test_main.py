import pytest as pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("playground", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "test when word is an isogram",
        "test when word is not an isogram",
        "function should be case-insensitive",
        "the empty string is an isogram",
    ]
)
def test_case_insensitivity(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
