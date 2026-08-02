import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("Adam", False),
        ("FFF", False),
        ("abc", True),
        ("Aabc", False),
        ("look", False),
        ("playground", True),
        ("abc123", True),
        ("abc111", False),
        ("False", True)
    ]
)
def test_should_return_correct_bool(word: str, result: bool) -> None:
    assert is_isogram(word) == result
