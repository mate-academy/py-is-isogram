import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("hello", False, id="consecutive repeated letters"),
        pytest.param("baby", False, id="non-consecutive repeated letters"),
        pytest.param("LlBb", False, id="different cases repeat"),
        pytest.param("halo", True, id="no repeats"),
        pytest.param("", True, id="empty string"),

    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
