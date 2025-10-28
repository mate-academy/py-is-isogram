import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="word with not repeat letters"),
        pytest.param("look", False, id="word with repeat letters"),
        pytest.param("Adam", False, id="word with repeat letters and A equals a"),
        pytest.param("", True, id="empty word"),
    ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
