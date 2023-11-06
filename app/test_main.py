import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "",
            True,
            id="check if func return True with empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="check if func return True with isogram string"
        ),
        pytest.param(
            "look",
            True,
            id="check if func return False with not isogram string"
        ),
        pytest.param(
            "Adam",
            True,
            id="check if func return False with not isogram string"
        ),
    ]
)
def test_get_correct_answers(word: str, result: bool) -> None:
    assert is_isogram(word) == result
