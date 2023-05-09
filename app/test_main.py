import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("playgrounds", True),
        ("", True),
        ("aDAm", False),
        ("floor", False)
    ]
)
def test_is_isogram(word: str,
                    expected: bool) -> None:
    error_message = f"Function should return {expected} when {word}"
    assert is_isogram(word) == expected, error_message
