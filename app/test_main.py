import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_count_value(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"Word: {word} is result {result}!"
