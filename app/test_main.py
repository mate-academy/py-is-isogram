import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="default isogram"),
        pytest.param("", True, id="empty string is isogram"),
        pytest.param(" ", True, id="one space string is isogram"),
        pytest.param("look", False, id="repeating letters, consecutive"),
        pytest.param("Adam", False, id="repeating letters, non-consecutive"),
        pytest.param("x", True, id="one letter"),
        pytest.param("++", False, id="non-letters used"),
        pytest.param("  qwe  zxc   ", False,
                     id="strange string with multiple spaces"),
        pytest.param("qwe zxc_tyu/jkl", True,
                     id="strange string with different symbols"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
