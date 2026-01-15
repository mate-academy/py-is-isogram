import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True,
                     id="Should check if all letters are different"),
        pytest.param("look", False,
                     id="Should check for repeating letters"),
        pytest.param("Adam", False,
                     id="Should check for case sensitivity"),
        pytest.param("", True,
                     id="Should check for an empty string")
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
