import pytest
from app.main import is_isogram


def test_playgrounds_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_look_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_adam_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_unique_letters() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_repeated_letter() -> None:
    assert is_isogram("alphabet") is False


@pytest.mark.parametrize("bad_input", [
    123,
    3.14,
    None,
    ["a", "b"],
])
def test_non_string_input_raises_attribute_error(bad_input: object) -> None:
    with pytest.raises(AttributeError):
        is_isogram(bad_input)
