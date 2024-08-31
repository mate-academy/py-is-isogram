from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "actual,expected",
    [
        (
            "Bob",
            False
        ),
        (
            "exhausting",
            True
        ),
        (
            "look",
            False
        ),
    ],
)
def test_the_output_should_be_equal_to_the_expectation(
        actual: str,
        expected: bool
) -> None:
    assert is_isogram(actual) == expected


def test_whole_quotes_is_isogram() -> None:
    assert is_isogram("") is True
