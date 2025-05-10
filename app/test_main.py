import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True,
                     id="The word dont have repeating letters"),
        pytest.param("look", False, id="The word have repeating letters"),
        pytest.param("Adam", False,
                     id="The word has the same letters in different cases. "),
        pytest.param("", True, id="Empty string is isogram")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
