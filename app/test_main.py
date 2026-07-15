from app import main
from pytest import mark


@mark.parametrize(
    "value, expected",
    [
        (" ", True),
        ("", True),
    ]
)
def test_is_isogram(value: str, expected: bool) -> None:
    assert main.is_isogram(value) == expected


@mark.parametrize(
    "value, expected",
    [
        ("abc", True),
        ("a", True),
        ("playground", True),
        ("isogram", True),
    ]
)
def test_is_isogram_with_unique_characters(value: str, expected: bool) -> None:
    assert main.is_isogram(value) == expected


@mark.parametrize(
    "value, expected",
    [
        ("hello", False),
        ("look", False),
        ("isogramm", False),
        ("isograms", False),
        ("  ", False),
    ]
)
def test_is_isogram_with_repeated_characters(
    value: str,
    expected: bool
) -> None:
    assert main.is_isogram(value) == expected


@mark.parametrize(
    "value, expected",
    [
        ("ABC", True),
        ("AA", False),
        ("Aa", False),
        ("aA", False),
        ("AbC", True),
        ("aBcD", True),
    ]
)
def test_is_isogram_case_sensitivity(value: str, expected: bool) -> None:
    assert main.is_isogram(value) == expected
