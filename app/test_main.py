import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("", True),
        pytest.param("Adam", False),
    ]
)
def test_correct_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result, f"For {word} result should be {result}"
