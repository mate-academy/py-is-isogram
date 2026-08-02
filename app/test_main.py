from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="valid"),
        pytest.param("lamp", True, id="valid"),
        pytest.param("", True, id="valid"),

        pytest.param("worldwide", False, id="non-consecutive"),
        pytest.param("alphabet", False, id="non-consecutive"),

        pytest.param("letter", False, id="consecutive"),
        pytest.param("book", False, id="consecutive"),

        pytest.param("leTter", False, id="different cases"),
        pytest.param("bOok", False, id="different cases"),

        pytest.param("       ", False, id="Empty string"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
