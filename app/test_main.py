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
def test_check_if_result_is_correct(word: str, result: bool) -> None:
    assert is_isogram(word) == result
