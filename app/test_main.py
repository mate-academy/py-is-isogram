import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="Empty string is an isogram"),
        pytest.param("playgrounds", True, id="All unique letters"),
        pytest.param("look", False, id="Repeating letters"),
        pytest.param("Adam", False, id="Case-insensitive repetition"),
        pytest.param("lads", True, id="Unique letters"),
        pytest.param("Machine", True, id="Case-insensitive unique letters"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected
