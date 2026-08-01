import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True),
        pytest.param("Adam", False),
        pytest.param("oreo", False),
        pytest.param("mortal", True),
        pytest.param("Texas", True),
        pytest.param("Anna", False),
        pytest.param("", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
