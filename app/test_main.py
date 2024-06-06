import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word,res",
    [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("grapesound", True),
        ("Ff", False),
        ("nice fabric", True),
        ("nice fab ric", False),
    ]
)
def test_is_isogram(input_word: str, res: bool) -> None:
    assert is_isogram(input_word) == res
