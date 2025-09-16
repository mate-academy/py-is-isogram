from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "text,expected_text",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("aA", False)
    ]
)
def test_isogram(text: str, expected_text: bool) -> None:
    assert is_isogram(text) is expected_text
