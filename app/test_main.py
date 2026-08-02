import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        (" ", True),
        ("  ", False),
        ("not false", True),
        ("only true, i swear", False)
    ]
)
def test_with_spaces(word: str, result: bool) -> None:
    assert (
        is_isogram(word) is result
    ), f"{word} should be {result}, look at spaces"


@pytest.mark.parametrize(
    "word, result",
    [
        ("SuPer", True),
        ("deDline", False),
        ("QWERTYqwerty", False),
        ("Rusni_pzD", True)
    ]
)
def test_with_upper_letters(word: str, result: bool) -> None:
    assert (
        is_isogram(word) is result
    ), f"{word} should be {result}, probably you have problems with uppercase"


def test_empty_string() -> None:
    assert (
        is_isogram("") is True
    ), "If string is empty it should result True"
