import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, is_isogram_result",
    [
        ("", True),
        ("playgrounds", True),
        ("Adam", False),
        ("adam", False),
        ("look", False),
        ("a", True),
        ("counterstrike", False)
    ]
)
def test_is_isogram(word: str, is_isogram_result: bool) -> None:
    assert is_isogram(word) == is_isogram_result


@pytest.mark.parametrize(
    "word",
    [
        1,
        None,
        [],
        {}
    ]
)
def test_wrong_type(word: int | None | list | dict) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
