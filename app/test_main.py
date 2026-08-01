import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    ["", "I", "Y3$", "Python", ":)"]
)
def test_should_return_true(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    ["balL", "horror", "Mom", "!:)!", "AC/DC"]
)
def test_should_return_false(word: str) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    [
        8,
        -5.9,
        True,
        False,
        ("yes",),
        ["y", "e", "s"],
        {"n", "o"},
        {"word": "word"}
    ]
)
def test_raises_exception_for_not_str(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
