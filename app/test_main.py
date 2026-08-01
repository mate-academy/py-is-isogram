import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("playGrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_eval(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
