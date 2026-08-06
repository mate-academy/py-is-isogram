import pytest
import app.main


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="isogram"),
        pytest.param("look", False, id="non-isogram"),
        pytest.param("Adam", False, id="non-isogram"),
        pytest.param("", True, id="empty-string"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert app.main.is_isogram(word) == expected
