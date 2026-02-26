import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram_basic(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
