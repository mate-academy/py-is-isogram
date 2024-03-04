import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, status",
    [
        ("Audi", True),
        ("Mercedes", False),
        ("Zaz", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, status: bool) -> None:
    assert is_isogram(word) is status
