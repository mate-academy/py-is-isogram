import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty string"),
        pytest.param("a", True, id="single letter"),
        pytest.param("playgrounds", True, id="simple isogram"),
        pytest.param("look", False, id="consecutive duplicate letters"),
        pytest.param("paparazzi", False,
                     id="multiple non-consecutive duplicates"),
        pytest.param("Adam", False, id="non-consecutive duplicate letters"),
        pytest.param("MaTe", True, id="mixed case isogram"),
        pytest.param("AcAdEmY", False, id="mixed case duplicate"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
