import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True,
                     id="test is isogram"),
        pytest.param("pLaYgRoundS", True,
                     id="function should be case-insensitive"),
        pytest.param("", True,
                     id="for this task, the empty string is an isogram"),
        pytest.param("look", False,
                     id="test is isogram"),
        pytest.param("Adam", False,
                     id="M and m are considered the same letter"),
    ]
)
def test_is_word_is_isogram(
    word: str,
    expected_result: bool
) -> None:
    assert is_isogram(word=word) == expected_result
