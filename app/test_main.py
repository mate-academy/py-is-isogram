import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_return_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result
