import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Shop", True),
        ("Adam", False),
        ("look", False),
        ("Baobab", False)
    ]
)
def test_is_isogram(
    word: str,
    expected: bool
) -> None:
    assert is_isogram(word) is expected
