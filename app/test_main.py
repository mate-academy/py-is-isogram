import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, result",
    [
        ("", True),
        ("abcdefg", True),
        ("book", False),
        ("isolation", False),
        ("Airplane", False)
    ],
    ids=[
        "empty",
        "unique lowercase",
        "repeating consecutive lowercase",
        "repeating non-consecutive lowercase",
        "repeating non-consecutive uppercase and lowercase"
    ]
)
def test_should_check_if_string_is_isogram_correctly(
        string: str,
        result: bool
) -> None:
    assert is_isogram(string) == result
