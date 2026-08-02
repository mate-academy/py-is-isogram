import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "words, result",
    [
        pytest.param("", True, id="empty string is an isogram"),
        pytest.param("playgrounds", True, id="All letters is different"),
        pytest.param("look", False, id="This word has same letters"),
        pytest.param("Adam", False, id="This word has same letters"),

    ]
)
def test_isogram(words: str, result: bool) -> None:
    assert is_isogram(words) == result
