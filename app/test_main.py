import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds",
                     True,
                     id="check when all letter another"),
        pytest.param("look",
                     False,
                     id="check when ward has same letter"),
        pytest.param("Adam",
                     False,
                     id="check case-insensitive"),
        pytest.param("",
                     True,
                     id="check empty str")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
