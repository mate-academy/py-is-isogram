from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    ("word", "result"),
    [
        ("playgrounds", True),
        ("Adam", False),
        ("", True),
        ("look", False)
    ]
)
def test_is_isogram_checks_correctly(word: str, result: bool) -> None:
    assert is_isogram(word) == result
