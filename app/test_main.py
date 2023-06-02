import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True,
                     id="default test with True result"),
        pytest.param("look", False,
                     id="default test with False result"),
        pytest.param("Adam", False,
                     id="default test with False result"),
        pytest.param("", True,
                     id="empty string")
    ]
)
def test_is_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
