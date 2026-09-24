import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        pytest.param("", True, id="empty string"),
        pytest.param("a", True, id="single letter"),
        pytest.param("equal", True, id="unique letters"),
        pytest.param("apply", False, id="consecutive duplicate"),
        pytest.param("WORLD", True, id="unique uppercase letters"),
        pytest.param("underground", False, id="non-consecutive duplicates"),
        pytest.param("PArameTRIzE", False, id="different case duplicate"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word=word) is expected
