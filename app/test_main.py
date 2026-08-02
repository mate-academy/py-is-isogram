import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("",
                     True,
                     id="empty string"),
        pytest.param("countryside",
                     True,
                     id="simple isogram"),
        pytest.param("Adam",
                     False,
                     id="string with different cases of the same letter"),
        pytest.param("food",
                     False,
                     id="consecutive letters"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
