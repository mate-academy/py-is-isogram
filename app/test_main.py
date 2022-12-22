from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "actual, expected",
    [
        (is_isogram('playgrounds'), True),
        (is_isogram('look'), False),
        (is_isogram('Adam'), False),
        (is_isogram(''), True)
    ]
)
def test_is_isogram(actual: bool, expected: bool) -> None:
    assert actual == expected
