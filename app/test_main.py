import pytest

from app.main import is_isogram


def test_cannot_use_is_isogram_with_int_as_word() -> None:
    with pytest.raises(AttributeError):
        is_isogram(word=5)


def test_cannot_use_is_isogram_with_float_as_word() -> None:
    with pytest.raises(AttributeError):
        is_isogram(word=5.2)


def test_cannot_use_is_isogram_with_bool_as_word() -> None:
    with pytest.raises(AttributeError):
        is_isogram(word=True)


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ],
    ids=[
        "empty word",
        "'playgrounds' word",
        "'look' word",
        "'Adam' word",
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"Word {word} is {result} isogram"
