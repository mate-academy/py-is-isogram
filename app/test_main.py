import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("Adam", False),
        ("look", False),
        ("playgrounds", True)
    ]
)
def test_get_current_results(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"When given {word} should return {result}"
