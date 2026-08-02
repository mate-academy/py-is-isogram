import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True,
                     id="Test long wold"),
        pytest.param("look", False,
                     id="Test double vowels"),
        pytest.param("Adam", False,
                     id="Test upper and double vowels"),
        pytest.param("", True,
                     id="Test empty string")
    ]
)
def test_is_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
