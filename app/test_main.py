import pytest
from app.main import is_isogram


def test_not_repeating_letters() -> None:
    assert is_isogram('playgrounds') == True


def test_consecutive_letters() -> None:
    assert is_isogram('look') == False


def test_not_consecutive_letters() -> None:
    assert is_isogram('Adam') == False


def test_with_empty_list() -> None:
    assert is_isogram('') == True


@pytest.mark.parametrize(
    "current_text, expected", [
        ('playgrounds' is True),
        ('look' is False),
        ('Adam' is False),
        ('' is True),
    ]
)
def test_various_case(current_text: str, expected: bool) -> None:
    assert is_isogram(current_text) == expected
