import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "words, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram_result(words: str, result: bool) -> None:
    assert is_isogram(words) == result
