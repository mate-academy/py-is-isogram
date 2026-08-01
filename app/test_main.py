import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),

    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word,result",
    [
        1,
        ["look", 34],
        None,

    ]
)
def invalid_input(word: str, result: bool) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
