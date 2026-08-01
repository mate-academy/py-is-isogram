from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, actual",
    [
        pytest.param("a", True, id="One letter"),
        pytest.param("", True, id="Empty string"),
        pytest.param("Adam", False, id="Letters big and small -> False"),
        pytest.param("PlayGrounds", True, id="Letters big and small -> True"),
        pytest.param("look", False, id="Adjacent identical letters -> False"),
    ]
)
def test_is_isogram(word: str, actual: bool) -> None:
    assert is_isogram(word) is actual

# write your code here
