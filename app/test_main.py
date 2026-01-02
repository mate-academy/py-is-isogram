import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True,
                     id="should return "),
        pytest.param("look", False,
                     id="should find consecutive repeating letters"),
        pytest.param("mom", False,
                     id="should find non-consecutive repeating letters"),
        pytest.param("Adam", False,
                     id="should be case-insensitive"),
        pytest.param("", True,
                     id="should return True"),
    ]
)
def test_word_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
