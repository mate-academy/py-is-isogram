import pytest
from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_main(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
