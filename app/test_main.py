from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True, id="basic-isogram"),
        pytest.param("look", False, id="non-isogram-repeated-o"),
        pytest.param("Adam", False, id="case-insensitive-repeated-a"),
        pytest.param("", True, id="empty-string"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
