import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True, id="`playgrounds` is isogram"),
        pytest.param("look", False, id="`look` is not isogram"),
        pytest.param("", True, id="empty string is isogram"),
        pytest.param("Area", False, id="`Area` is isogram"),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
