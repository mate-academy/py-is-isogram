import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expect",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, expect: bool) -> None:
    assert is_isogram(word) == expect
