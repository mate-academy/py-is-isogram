from app import main

# write your code here
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="test_1"),
        pytest.param("Adam", False, id="case_insensitive"),
        pytest.param("", True, id="empty_string"),
        pytest.param("abcda", False, id="non_consecutive_letters"),
        pytest.param("aabb", False, id="consecutive_letters"),
    ],
)
def test_is_isogram(
    word: str,
    result: bool,
) -> None:
    assert main.is_isogram(word) == result
