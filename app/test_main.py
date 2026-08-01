import pytest
from app.main import is_isogram


def test_not_repeating_letters() -> None:
    assert is_isogram("playgrounds")


def test_consecutive_letters() -> None:
    assert not is_isogram("look")


def test_not_consecutive_letters() -> None:
    assert not is_isogram("Adam")


def test_with_empty_list() -> None:
    assert is_isogram("")


@pytest.mark.parametrize(
    "current_text, expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_various_case(current_text: str, expected: bool) -> None:
    assert is_isogram(current_text) == expected
