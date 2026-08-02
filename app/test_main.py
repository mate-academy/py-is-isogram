import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word",
    [
        7,
        None,
        6.7
    ]
)
def test_is_isogram_raises_attribute_error(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
