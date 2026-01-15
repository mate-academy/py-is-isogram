import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,is_isogram_word",
    [
        pytest.param("playgrounds", True, id="is isogram"),
        pytest.param("look", False, id="is not isogram"),
        pytest.param("Adam", False, id="not isogram with upper case char"),
        pytest.param("", True, id="empty string is isogram"),
    ]
)
def test_is_isogram(
        word: str,
        is_isogram_word: bool
) -> None:
    assert is_isogram(word) == is_isogram_word
