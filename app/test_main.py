import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("playgrounds", True),
        ("isogram", True),
        ("look", False),
        ("letter", False),
        ("Adam", False),
        ("AlAbA", False),
        ("a", True),
        ("Z", True),
        ("PlayGrounds", True),
        ("Look", False),
    ]
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
