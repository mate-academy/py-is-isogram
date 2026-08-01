import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("", True,
                     id="Empty string is an isogram."),
        pytest.param("Adam", False,
                     id="Word 'Adam' string is not an isogram. ('A' != 'a')"),
        pytest.param("look", False,
                     id="Word 'look' string is not an isogram. ('o' == 'o')"),
        pytest.param("playgrounds", True,
                     id="Word 'playgrounds' string is an isogram.")
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
