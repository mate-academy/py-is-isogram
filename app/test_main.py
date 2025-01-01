import pytest

from app.main import is_isogram


def test_correct_error_raised() -> None:
    with pytest.raises(AttributeError):
        is_isogram(123)


@pytest.mark.parametrize(
    "word, result",
    [
        ("Apache", False),
        ("", True),
        ("look", False),
        ("123", True),
        (" cake ", False)
    ],
    ids=[
        "Should be case insencitive",
        ("Empty string is isogram"),
        ("Word with two same chars is not isogram"),
        ("Should worr with str numbers"),
        ("whitespace considered as char")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"{word} should result {result}"
