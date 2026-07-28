import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("isogram", True),
        ("", True),
        ("test", False),
        ("github", True),
        ("   function   ", False),
        ("look", False),
        ("LoOk", False),
        ("FlakE", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
