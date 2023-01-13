import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="isogram"),
        pytest.param("look", False, id="with repeated letters"),
        pytest.param("Adam", False, id="with repeated letters in different registers"),
        pytest.param("", True, id="empty string")
    ]
)
def test_should_return_correct_answer(word: str, result: bool) -> None:
    assert (is_isogram(word) == result)
