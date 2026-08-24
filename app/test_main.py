import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("playgrounds", True),
        ("BACKGROUND", True),
        ("English word!", True),
        ("Six year old", False),
        ("fool", False),
        ("Sister", False)
    ]
)
def test_isogram_word(word: str, result: bool) -> None:
    assert is_isogram(word) == result
