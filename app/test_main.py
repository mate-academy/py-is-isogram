import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("wood", False),
        ("test", False),
        ("daughter", True),
        ("Coach", False),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
