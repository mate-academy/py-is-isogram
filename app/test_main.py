import pytest

from app.main import is_isogram


@pytest.mark.parametrize("text, expected", [
    pytest.param("playgrounds",
                 True,
                 id="word without equal letters is isogram"),
    pytest.param("look",
                 False,
                 id="word with equal letters is not isogram"),
    pytest.param("Adam",
                 False,
                 id="case sensitive characters in isogram are equal"),
    pytest.param("",
                 True,
                 id="empty string is isogram"),
])
def test_is_isogram(text: str, expected: bool) -> None:
    assert is_isogram(text) == expected
