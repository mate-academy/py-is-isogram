import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("Adam", False,
                     id="when given a word with 2 letters of different case"),
        pytest.param("playgrounds", True,
                     id="when given a long string"),
        pytest.param("door", False,
                     id="when given a word of 2 letters of the same case"),
        pytest.param("", True,
                     id="when given empty string"),
        pytest.param("Y", True,
                     id="when given 1 letter"),
        pytest.param(" space ", False,
                     id="when two spaces are given"),
    ]
)
def test_check_function_for_given_string(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
