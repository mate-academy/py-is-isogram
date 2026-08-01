import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,really",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_word_checked_correctly(word: str, really: bool) -> None:
    assert (
        is_isogram(word) == really
    ), f"Is {word} an isogram? {really}."


@pytest.mark.parametrize(
    "word",
    [
        (1),
        ([1, 1, 0, 0]),
        ({"cents": 101}),
    ],
    ids=[
        "int",
        "list",
        "dict",
    ]
)
def test_word_is_string(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
