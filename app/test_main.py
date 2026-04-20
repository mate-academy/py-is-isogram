from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_result_correctness(word: str,
                            result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"Word: '{word}' should be: {result}"


@pytest.mark.parametrize(
    "word,result",
    [
        ("play2times", False),
        ("look at you", False),
        ("45354", False)
    ]
)
def test_only_letters(word: str,
                      result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"Word: '{word}' should contain only letters"
