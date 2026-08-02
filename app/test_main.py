import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("word", True),
        ("Wow", False),
        ("apple", False),
        ("lemon", True),
        ("atmosphere", False),
        ("Gang", False),
        ("", True)
    ],
    ids=[
        "All letters are different it's an isogram",
        "Function should be case-insensitive",
        "There is two or more the same letters it's not an isogram",
        "All letters are different it's an isogram",
        "There is two or more the same letters it's not an isogram",
        "Function should be case-insensitive",
        "An empty string is an isogram"
    ]
)
def test_is_isogram_works_correctly(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
