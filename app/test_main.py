import pytest
from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_playgrounds_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_look_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_adam_is_not_isogram() -> None:
    assert is_isogram("Adam") is False


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Dermatoglyphics", True),
        ("aba", False),
        ("moOse", False),
    ]
)
def test_is_isogram_parametrized(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
