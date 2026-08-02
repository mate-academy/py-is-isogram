from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),


    ]
)
def test_is_isogram_various_thresholds(
        word: int,
        expected_result: bool) -> None:
    assert (
           is_isogram(word) == expected_result)\
        , f"Should return {expected_result} for word {word})"
