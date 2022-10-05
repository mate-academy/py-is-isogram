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
def test_is_inogram(word: str, expect: bool):
    assert is_isogram(word) == expect
