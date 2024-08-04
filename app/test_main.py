import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("hOnor", False),
        ("3-cjLo,s/duZ=1", True),
        ("    we go    ", False),
        ("hello!", False)
    ],
    ids=[
        "if empty string is given",
        "ignoring register and if non-consecutive",
        "if no symbol is repeated",
        "when `spaces` repeats",
        "if the same symbol follows the same"
    ]
)
def test_should_return_correct_result(
    word: str,
    expected: bool
) -> None:
    assert is_isogram(word) == expected


def test_should_raise_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(123)


def test_argument_reference_must_refer_to_the_same_string() -> None:
    word = "WoRd!"
    is_isogram(word)
    assert word == "WoRd!"
