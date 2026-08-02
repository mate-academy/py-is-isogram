import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("", True,
                     id="the empty string is an isogram"),
        pytest.param("ambidextrously", True,
                     id="word with no repeating letters is isogram"),
        pytest.param("dialogue", True,
                     id="word with no repeating letters is isogram"),
        pytest.param("book", False,
                     id="word with repeating letters is no isogram"),
        pytest.param("Memory", False,
                     id="word with repeating letters is no isogram"),
        pytest.param("DIALOGUE", True,
                     id="should be case-insensitive"),
        pytest.param("MEMORY", False,
                     id="should be case-insensitive"),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
