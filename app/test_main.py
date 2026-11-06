from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word",
    [
        (15),
        (15.5),
        ([15]),
        ({15}),
        (None),
        (True)
    ]
)
def test_word_incorrect_type_raises_type_error(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)


def test_test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("ABab", False),
        ("adam", False)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
