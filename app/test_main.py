import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty_string"),
        pytest.param("isogram", True, id="isogram"),
        pytest.param("hello", False, id="not_isogram_consecutive"),
        pytest.param("world", True, id="isogram_world"),
        pytest.param("playgrounds", True, id="isogram_playgrounds"),
        pytest.param("look", False, id="not_isogram_look"),
        pytest.param("Adam", False, id="not_isogram_non_consecutive"),
        pytest.param("Mm", False, id="not_isogram_case_insensitive"),
        pytest.param("Moom", False, id="not_isogram_case_insensitive_mixed"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
