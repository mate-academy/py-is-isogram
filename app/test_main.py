import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="test valid word"),
        pytest.param("Look", False, id="test consecutive letters"),
        pytest.param("loto", False, id="test non-consecutive letters"),
        pytest.param(
            "Adam", False, id="test non-consecutive letters in different cases"
        ),
        pytest.param("", True, id="test empty string")
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
