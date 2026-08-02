from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_should_return_expected_values(word: str, result: int) -> None:
    assert (
        is_isogram(word) == result
    ), (
        f"if cents == {word}, result should be {result}"
    )
