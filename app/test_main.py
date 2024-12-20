from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="isogram value"),
        pytest.param('look', False, id="not isogram value"),
        pytest.param("Adam", False, id="difference cases in words"),
        pytest.param("", True, id="empty string"),

    ]
)
def test_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) is result
