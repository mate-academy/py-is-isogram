import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result", [
        pytest.param("", True,
                     id="empty line"),
        pytest.param("playgrounds", True,
                     id="no repeating letters"),
        pytest.param("look", False,
                     id="same consecutive letters"),
        pytest.param("Adam", False,
                     id="same non-consecutive letters"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
