import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("new", True, id="Check that word is isogram"),
        pytest.param("look", False, id="Check word is not isogram"),
        pytest.param("Adam", False, id="Check function is case-insensitive"),
        pytest.param("", True, id="Check that empty string is isogram")
    ]
)
def test_find_isogram_correctly(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
